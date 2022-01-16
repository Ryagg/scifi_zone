from django.shortcuts import render, redirect, get_object_or_404
from tickets.models import Ticket

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')



def add_to_bag(request, item_id):
    """ Add the selected ticket to the shopping bag """

    ticket = get_object_or_404(Ticket, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        bag[item_id] += 1
    else:
        bag[item_id] = 1

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
