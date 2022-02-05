from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from tickets.models import Ticket

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')



def add_to_bag(request, item_id):
    """ Add the selected ticket to the shopping bag """

    ticket = get_object_or_404(Ticket, pk=int(item_id))
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity # replaces quantity instead of adding it
        messages.success(request, f'Updated {ticket.name} quantity to \
            {bag[item_id]}.')
    else:
        bag[item_id] = quantity # works as intended
        messages.success(request, f'Added {ticket.name} x {quantity} \
            to your bag.')

    request.session['bag'] = bag
    print(request.session['bag'])

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove item from bag """
    try:
        ticket = get_object_or_404(Ticket, pk=int(item_id))
        bag = request.session.get('bag', {})

        del bag[item_id]
        messages.success(request, f'Removed {ticket.name} from your bag.')

        request.session['bag'] = bag
        print(request.session['bag'])
        return redirect(reverse('view_bag'))

    except Exception as error:
        return HttpResponse(status=500,content=error)
