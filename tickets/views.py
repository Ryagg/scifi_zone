from django.shortcuts import render, get_object_or_404
from .models import Ticket, Package, Actor

# pylint: disable=locally-disabled, no-member

def all_tickets(request):
    """ A view to show all tickets """

    tickets = Ticket.objects.filter(name__icontains='Ticket')

    context = {
    'tickets': tickets,
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
