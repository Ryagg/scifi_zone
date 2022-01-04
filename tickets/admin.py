from django.contrib import admin
from .models import Ticket, Category

class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'category',
        'image',
    )

    # has to be a tuple because sorting on multiple columns is possible
    ordering = ('sku',) # to reverse the order stick a minus in front


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Category, CategoryAdmin)
