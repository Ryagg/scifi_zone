from django.shortcuts import render
from .models import Ticket

def all_tickets(request):
    """ A view to show all tickets """

    tickets = Ticket.objects.all()

    context = {
    'tickets': tickets,
    }

    return render(request, 'tickets/tickets.html', context)
