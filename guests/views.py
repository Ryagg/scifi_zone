from django.shortcuts import render, get_object_or_404
from tickets.models import Actor, Ticket

def view_all_guests(request):
    """A view to show all guests holding panels at the convention"""

    actors = Actor.objects.all()

    context = {
        'actors': actors,
    }

    return render(request, 'guests/guests.html', context)


def guest_detail(request, actors_id):
    """ A view to show detailed actor information """

    actors = Actor.objects.all()
    actor = get_object_or_404(Actor, pk=actors_id)
    tickets = Ticket.objects.all()
    # autograph_price_category = f'Autograph Ticket Price Category {actor.star_autograph_category}'

    context = {
        'actors': actors,
        'actor': actor,
        'tickets': tickets,
        # 'autograph_price_category': autograph_price_category,
    }
    print(actor.star_autograph_category)
    return render(
        request, 'guests/guest_detail.html', context)
