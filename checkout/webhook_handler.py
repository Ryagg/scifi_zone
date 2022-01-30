import json
import time

from django.http import HttpResponse
from tickets.models import Ticket
from profiles.models import UserProfile
from .models import Order, OrderLineItem


# pylint: disable=locally-disabled, no-member

class StripeWebhookHandler:
    """Handle Stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        print('unhandled webhook received')
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        print(intent)

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None # allow anonymous users to checkout
        username = intent.metadata.username
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
            # self._send_confirmation_email(order)
            print('order already in database')
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
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
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        print('payment_intend succeeded')
        return HttpResponse(content=f'Webhook received: {event["type"]}',
        status=200)

    def handle_payment_intent_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        print('payment failed')
        return HttpResponse(content=f'Webhook received: {event["type"]}',
        status=200)
