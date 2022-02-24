from decimal import Decimal
from django.shortcuts import get_object_or_404
from scifi_zone.settings import VAT_PERCENTAGE
from tickets.models import Ticket


def bag_contents(request):
    """Updates bag and makes contents available"""

    bag_items = []
    quantity = 0
    item_count = 0
    grand_total = 0
    vat = 0

    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            ticket = get_object_or_404(Ticket, pk=item_id)
            grand_total += item_data * ticket.price
            item_count += item_data
            vat = ((grand_total * VAT_PERCENTAGE) / 100)
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'ticket': ticket,
                'item_count': item_count,
            })
        else:
            ticket = get_object_or_404(Ticket, pk=item_id)
            for selection, quantity in item_data['items_by_selected'].items():
                grand_total += quantity * ticket.price
                item_count += quantity
                vat = ((grand_total * VAT_PERCENTAGE) / 100)
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'ticket': ticket,
                    'item_count': item_count,
                    'selection': selection,
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
