from django.shortcuts import render
from tickets.models import Actor

# pylint: disable=locally-disabled, no-member


def index(request):
    """ A view to return the index page """

    actors = Actor.objects.all()
    actor_count = len(actors)
    midway = actor_count / 2

    context = {
        'actors': actors,
        'actor_count': actor_count,
        'midway': midway,
    }
    return render(request, 'home/index.html', context)


def timetable(request):
    """ A view to return the time table page """

    return render(request, 'home/timetable.html')


def site_notice(request):
    """ A view to return the site notice page """

    return render(request, 'home/site_notice.html')


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')
