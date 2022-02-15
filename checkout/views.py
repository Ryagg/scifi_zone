import json
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
from bag.contexts import bag_contents
from tickets.models import Ticket
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from .forms import OrderForm
from .models import Order, OrderLineItem

# pylint: disable=locally-disabled, no-member, using-constant-test


def _send_confirmation_email(order):
    """Send the user a confirmation email"""
    cust_email = order.email
    # remove newlines to prevent BadHeaderError
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order}).replace('\n', '')
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


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
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        print('cache_checkout_data')
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, 'Sorry, your payment cannot be processed \
            right now. Please try again later.')
        return HttpResponse(content=error, status=400)


def checkout(request):
    """Get infos from the order form and create an order in the database"""

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
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            ticket=ticket,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for selection, quantity in item_data[
                            'items_by_selected'].items():
                            order_line_item = OrderLineItem(
                            order=order,
                            ticket=ticket,
                            quantity=quantity,
                            selection=selection,
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
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            payment_method_types=["card"],
        )

        # Attempt to prefill the from with info from the user's profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'city': profile.default_city,
                    'postcode': profile.default_postcode,
                    'state': profile.default_state,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm

        template = "checkout/checkout.html"
        context = {
            "order_form": order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            # 'redirect': redirect,
        }

        print('reached end of checkout')
        return render(request, template, context)


def checkout_success(request, order_number):
    """Handle successfull checkouts"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    profile = UserProfile.objects.get(user=request.user)
    order.user_profile = profile
    order.save()
    print('order processed')

    # Save the user's info
    if save_info:
        profile_data = {
            'default_email': order.email,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_city': order.city,
            'default_postcode': order.postcode,
            'default_state': order.state,
            'default_country': order.country,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Your order {order_number} has been \
        successfully processed. We will send a confirmation email to \
            {order.email} shortly.')
    _send_confirmation_email(order)

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    print('Order received and processed')
    return render(request, template, context)
