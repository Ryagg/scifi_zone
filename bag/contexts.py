from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tickets.models import Ticket

def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0
    grand_total = 0

    bag = request.session.get('bag', {})

    for item_id in bag.items():
        ticket = get_object_or_404(Ticket, pk=item_id)
        total += 1
        bag_items.append({
            'item_id': item_id,
            'ticket': ticket,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context
