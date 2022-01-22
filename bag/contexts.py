from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from scifi_zone.settings import VAT_PERCENTAGE
from tickets.models import Ticket

def bag_contents(request):

    bag_items = []
    quantity = 0
    item_count = 0
    grand_total = 0
    vat = 0

    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        ticket = get_object_or_404(Ticket, pk=item_id)
        grand_total += quantity * ticket.price
        item_count += quantity
        vat = ((grand_total * VAT_PERCENTAGE)/100)

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'ticket': ticket,
            'item_count': item_count,
        })

    context = {
        'bag_items': bag_items,
        'quantity': quantity,
        'item_count': item_count,
        'grand_total': grand_total,
        'vat': vat,
        'VAT_PERCENTAGE': VAT_PERCENTAGE
    }

    return context
