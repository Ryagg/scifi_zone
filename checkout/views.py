from django.shortcuts import render, redirect, reverse,get_object_or_404
from django.contrib import messages
from django.conf import settings

import stripe

from bag.contexts import bag_contents
from .forms import OrderForm
from .models import Order, OrderLineItem

from tickets.models import Ticket

# pylint: disable=locally-disabled, no-member

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
            order = order_form.save()
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
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse(
                    'checkout_success',
                    args=[
                        order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(request, "Your bag is empty.")
            return redirect(reverse("tickets"))

        order_form = OrderForm()

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount = stripe_total,
            currency = settings.STRIPE_CURRENCY,
        )

        template = "checkout/checkout.html"
        context = {
            "order_form": order_form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret,

        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """Handle successfull checkouts"""
    save_info = request.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order {order_number} has been \
        successfully processed. We will send a confirmation email to \
            {order.email} shortly.')

    if 'bag' in request.session:
        del request.sesion['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
