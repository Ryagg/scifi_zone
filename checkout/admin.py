from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ("order_number", "date", "grand_total", "original_bag",
                       "stripe_pid")

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "sub_total",
        "grand_total",
        "street_address1",
        "street_address2",
        "city",
        "state",
        "postcode",
        "country",
        "original_bag",
        "stripe_pid"
    )

    # restrict columns that show up in the order list
    list_display = (
        "order_number",
        "date",
        "full_name",
        "email",
        "grand_total")

    # use reverse chronological order
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
