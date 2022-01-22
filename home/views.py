from django.shortcuts import render
from tickets.models import Actor

# pylint: disable=locally-disabled, no-member

def index(request):
    """ A view to return the index page """

    actors = Actor.objects.all()

    context = {
        'actors': actors,
    }

    return render(request, 'home/index.html', context)
