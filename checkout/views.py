import json
from django.shortcuts import render, redirect, reverse,get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
from bag.contexts import bag_contents
from tickets.models import Ticket
from .forms import OrderForm
from .models import Order, OrderLineItem



# pylint: disable=locally-disabled, no-member

@require_POST
def cache_checkout_data(request):
    try:
        # get payment intent id
        pid = request.POST.get('client_secret').split('_secret')[0]
        # set up stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # tell stripe what we want to modify
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            # 'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        print('cache_checkout_data')
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, 'Sorry, your payment cannot be processed \
            right now. Please try again later.')
        return HttpResponse(content=error, status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'city': request.POST['city'],
            'postcode': request.POST['postcode'],
            'state': request.POST['state'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid:
            # prevent multiple save events
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            print(order)
            for item_id, item_data in bag.items():
                try:
                    ticket = Ticket.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order = order,
                        ticket = ticket,
                        quantity = item_data,
                    )
                    order_line_item.save()
                except Ticket.DoesNotExist:
                    messages.error(request, (
                        "One or more of the tickets in your bag couldn't be \
                            found in our database. Please contact us!")
                            )
                    order.delete()
                    print('order deleted')
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            print('checkout success!')
            return redirect(
                reverse(
                    'checkout_success',
                    args=[
                        order.order_number]))

        else:
            print('form error')
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get("bag", {})
        if not bag:
            print('bag empty')
            messages.error(request, "Your bag is empty.")
            return redirect(reverse("tickets"))



        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount = stripe_total,
            currency = settings.STRIPE_CURRENCY,
            automatic_payment_methods={
                'enabled': True,
            },
        )

        order_form = OrderForm()
        template = "checkout/checkout.html"
        context = {
            "order_form": order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'redirect': redirect,


        }

        print('reached end of checkout')
        return render(request, template, context)


def checkout_success(request, order_number):
    """Handle successfull checkouts"""
    # save_info = request.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    print('order processed')
    messages.success(request, f'Your order {order_number} has been \
        successfully processed. We will send a confirmation email to \
            {order.email} shortly.')

    if 'bag' in request.session:
        del request.sesion['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    print('Order received and processed')
    return render(request, template, context)
