from django.shortcuts import render
from tickets.models import Actor

def view_all_guests(request):
    """A view to show all guests holding panels at the convention"""

    actors = Actor.objects.all()

    context = {
        'actors': actors,
    }

    return render(request, 'guests/guests.html', context)
