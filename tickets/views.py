from django.shortcuts import render, get_object_or_404
from .models import Ticket, Actor

def all_tickets(request):
    """ A view to show all tickets """

    tickets = Ticket.objects.all()

    context = {
    'tickets': tickets,
    }

    return render(request, 'tickets/tickets.html', context)


def ticket_detail(request, tickets_id):
    """ A view to show detailed ticket information """

    ticket = get_object_or_404(Ticket, pk=tickets_id)
    goodies = ticket.included.split(',')
    actors = Actor.objects.all()



    context = {
        'ticket': ticket,
        'goodies': goodies,
        'actors': actors,

    }
    print(ticket)
    return render(request, 'tickets/ticket_detail.html', context)
