from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from guests.forms import ActorForm
from tickets.models import Actor, Ticket

# pylint: disable=locally-disabled, no-member


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

    context = {
        'actors': actors,
        'actor': actor,
        'tickets': tickets,
    }
    print(actor.star_autograph_category)
    return render(
        request, 'guests/guest_detail.html', context)


@login_required
def add_guest(request):
    """Add an actor to the guests at the convention"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to add \
        guests. Feel free to contact us with your suggestions!")
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            actor = form.save()
            messages.success(request, 'New actor added!')
            return redirect(reverse('guest_detail', args=[actor.id]))
        else:
            messages.error(request, 'Actor could not be added! \
                Please check the form input.')
    else:
        # avoid wiping out the form errors
        form = ActorForm()

    template = 'guests/add_guest.html'
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_guest_info(request, actors_id):
    """Edit the info about an actor at the convention"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to edit \
        information about our guests. Feel free to contact us with \
        your suggestions!")
        return redirect(reverse('home'))
    actor = get_object_or_404(Actor, pk=actors_id)
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES, instance=actor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guest info updated!')
            return redirect(reverse('guest_detail', args=[actor.id]))
        else:
            messages.error(request, 'Guest info could not be updated! \
                Please check the form input.')
    else:
        # avoid wiping out the form errors
        form = ActorForm(instance=actor)
        messages.info(request, f'You are editing the info about {actor.name}')

    template = 'guests/edit_guest_info.html'
    context = {
        "form": form,
        "actor": actor,
    }

    return render(request, template, context)


@login_required
def remove_guest(request, actors_id):
    """Remove the guest from the convention"""
    if not request.user.is_superuser:
        messages.error(request, "You don't have permission to remove \
        guests from the event!")
        return redirect(reverse('home'))
    actor = get_object_or_404(Actor, pk=actors_id)
    actor.delete()
    messages.success(request, 'Guest removed!')
    return redirect(reverse('guests'))
