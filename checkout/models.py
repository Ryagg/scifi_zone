import uuid

from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField
from tickets.models import Ticket
from profiles.models import UserProfile

# pylint: disable=locally-disabled, no-member


class Order(models.Model):
    """
    The order model contains all fields and functions needed to complete an
    order
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    street_address1 = models.CharField(max_length=60, null=False, blank=False)
    street_address2 = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=60, null=True, blank=True)
    postcode = models.CharField(max_length=16, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    email = models.EmailField(max_length=160, null=False, blank=False)
    sub_total = models.DecimalField(
        max_digits=6, decimal_places=0, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=6, decimal_places=0, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """Generate a random, unique order number using UUID"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update grand total with each newly added item"""
        self.grand_total = self.lineitems.aggregate(Sum("lineitem_total"))[
            "lineitem_total__sum"
        ] or 0
        self.save()

    def save(self, *args, **kwargs):
        """Override the original save method to set the order number
        if it doesn't yet exist"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    A model for each row of an order that stores the item, quantity, and
    subtotal for the item
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    ticket = models.ForeignKey(
        Ticket, null=False, blank=False, on_delete=models.CASCADE
    )
    selection = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=0, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.ticket.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.ticket.sku} on order {self.order.order_number}"
