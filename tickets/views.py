from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages

from django.db.models import Q
from .models import Ticket, Actor

# pylint: disable=locally-disabled, no-member

def all_tickets(request):
    """ A view to show all tickets """

    tickets = Ticket.objects.filter(name__icontains='Ticket')
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]

            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('tickets'))

            # return results where the query is matched in name OR description
            queries = Q(
                name__icontains=query) | Q(
                description__icontains=query)
            tickets = tickets.filter(queries)

    context = {
    'tickets': tickets,
    "search_term": query,
    }

    return render(request, 'tickets/tickets.html', context)

def ticket_detail(request, tickets_id):
    """ A view to show detailed ticket information """

    ticket = get_object_or_404(Ticket, pk=tickets_id)
    price_category = ticket.price_category
    goodies = ticket.included.split(',')
    actors = Actor.objects.all()

    context = {
        'ticket': ticket,
        'price_category': price_category,
        'goodies': goodies,
        'actors': actors,

    }
    print(ticket)
    return render(request, 'tickets/ticket_detail.html', context)


def all_packages(request):
    """ A view to show all packages """

    packages = Ticket.objects.filter(name__icontains='Package')

    context = {
        'packages': packages,
    }

    return render(request, 'tickets/packages.html', context)

def package_detail(request, package_id, package_name):
    """ A view to show detailed package information """

    package = get_object_or_404(Ticket, pk=package_id, name=package_name)
    goodies = package.included.split(',')

    context = {
        'package': package,
        'goodies': goodies,
    }

    return render(request, 'tickets/package_detail.html', context)
