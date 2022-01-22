from django.db import models
from tickets.models import Ticket


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    street_address1 = models.CharField(max_length=60, null=False, blank=False)
    street_address2 = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=60, null=True, blank=True)
    postcode = models.CharField(max_length=16, null=False, blank=False)
    country = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=160, null=False, blank=False)
    sub_total = models.DecimalField(max_digits=6, decimal_places=0,
        null=False, default=0)
    grand_total = models.DecimalField(max_digits=6, decimal_places=0,
        null=False, default=0)


class OrderLineItem(models.Model):

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
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=0, null=False, blank=False, editable=False
    )
