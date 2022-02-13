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
            form.save()
            messages.success(request, 'New actor added!')
            return redirect(reverse('add_guest'))
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
