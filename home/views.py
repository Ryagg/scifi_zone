from django.shortcuts import render

from tickets.models import Actor

def index(request):
    """ A view to return the index page """

    actors = Actor.objects.all()

    context = {
        'actors': actors,
    }

    return render(request, 'home/index.html', context)
