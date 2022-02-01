import json, time
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import stripe

from tickets.models import Ticket
from profiles.models import UserProfile
from .models import Order, OrderLineItem

# pylint: disable=locally-disabled, no-member

def _send_confirmation_email(order):
    """Send the user a confirmation email"""
    cust_email = order.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order})
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
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as error:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as error:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as error:
        return HttpResponse(content=error, status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object # contains a stripe.PaymentIntent
        handle_payment_intent_succeeded(payment_intent)
    # Then define and call a method to handle the successful payment intent.
    # handle_payment_intent_succeeded(payment_intent)
    else:
        print(f'Unhandled Webhook received: {event["type"]}')
        handle_payment_intent_failed(event)

    return HttpResponse(status=200)

def handle_payment_intent_succeeded(payment_intent):
    """Handle the payment_intent.succeeded webhook from Stripe"""
    pid = payment_intent.id
    bag = payment_intent.metadata.bag
    save_info = payment_intent.metadata.save_info
    print(payment_intent)

    billing_details = payment_intent.charges.data[0].billing_details
    shipping_details = payment_intent.shipping
    grand_total = round(payment_intent.charges.data[0].amount / 100, 2)

    # Clean data in the shipping details
    for field, value in shipping_details.address.items():
        if value == "":
            shipping_details.address[field] = None

    # Update profile information if save_info was checked
    profile = None # allow anonymous users to checkout
    username = payment_intent.metadata.username
    if username != 'AnonymousUser':
        profile = UserProfile.objects.get(user__username=username)
        if save_info:
            profile.default_street_address1 = shipping_details.address.line1
            profile.default_street_address2 = shipping_details.address.line2
            profile.default_postcode = shipping_details.address.post_code
            profile.default_city = shipping_details.address.city
            profile.default_state = shipping_details.address.state
            profile.default_country = shipping_details.address.country
            profile.save()


    order_exists = False
    attempt = 1
    while attempt <= 5:
        try:
            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=billing_details.email,
                street_address1__iexact=shipping_details.address.line1,
                street_address2__iexact=shipping_details.address.line2,
                city__iexact=shipping_details.address.city,
                postcode__iexact=shipping_details.address.postal_code,
                state=shipping_details.address.state,
                country__iexact=shipping_details.address.country,
                grand_total=grand_total,
                original_bag=bag,
                stripe_pid=pid,
            )
            order_exists = True
            break
        except Order.DoesNotExist:
            attempt += 1
            time.sleep(1)
    if order_exists:
        _send_confirmation_email(order)
        print('order already in database')
        return HttpResponse(
            content='Webhook received: | SUCCESS: Verified order already in database',
            status=200)
    else:
        order = None
        try:
            order = Order.objects.create(
                full_name=shipping_details.name,
                user_profile=profile,
                email=billing_details.email,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                city=shipping_details.address.city,
                postcode=shipping_details.address.postal_code,
                state=shipping_details.address.state,
                country=shipping_details.address.country,
                grand_total=grand_total,
                original_bag=bag,
                stripe_pid=pid,
            )
            for item_id, item_data in json.loads(bag).items():
                ticket = Ticket.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    ticket=ticket,
                    quantity=item_data,
                )
                order_line_item.save()

        except Exception as e:
            if order:
                order.delete()
            print('order deleted')
            return HttpResponse(
                content=f'Webhook received | ERROR: {e}',
                status=500)

    print('payment_intend succeeded')
    # self._send_confirmation_email(order)
    return HttpResponse(
        content='Webhook received | SUCCESS: Created order in webhook',
    status=200)

def handle_payment_intent_failed(event):
    """Handle the payment_intent.payment_failed webhook from Stripe"""
    print(f'payment failed {event}')
    return HttpResponse(content='Webhook received',
    status=200)
