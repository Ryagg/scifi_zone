from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse,
    HttpResponse,
)
from django.contrib import messages
from tickets.models import Ticket


def view_bag(request):
    """A view that renders the bag contents page"""
    return render(request, "bag/bag.html.jinja")


def add_to_bag(request, item_id):
    """Add the selected ticket to the shopping bag"""

    ticket = get_object_or_404(Ticket, pk=int(item_id))
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    selected = None
    if "chosen_actor" in request.POST:
        selected = request.POST["chosen_actor"]
    bag = request.session.get("bag", {})

    if selected:
        if item_id in bag:
            if selected in bag[item_id]["items_by_selected"].keys():
                bag[item_id]["items_by_selected"][selected] += quantity
                messages.success(
                    request,
                    f"Updated {ticket.name} quantity "
                    f"for {selected} to "
                    f'{bag[item_id]["items_by_selected"][selected]}',
                )
                print(request.session["bag"])
            else:
                bag[item_id]["items_by_selected"][selected] = quantity
                messages.success(
                    request,
                    f"Added {ticket.name} x {quantity} "
                    f" for {selected} to your bag.",
                )
                print(request.session["bag"])
        else:
            bag[item_id] = {"items_by_selected": {selected: quantity}}
            messages.success(
                request,
                f"Added {ticket.name} x {quantity} "
                f" for {selected} to your bag!",
            )
            print(bag)
    else:
        if item_id in bag:
            bag[item_id] += quantity
            messages.success(
                request,
                f"Updated {ticket.name} quantity to \
                {bag[item_id]}.",
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                f"Added {ticket.name} x {quantity} \
                to your bag.",
            )

    request.session["bag"] = bag

    return redirect(redirect_url)


def update_bag(request, item_id):
    """Update quantity of selected bag item to user's choice"""

    ticket = get_object_or_404(Ticket, pk=int(item_id))
    quantity = int(request.POST.get("quantity"))
    selected = None
    if "chosen_actor" in request.POST:
        selected = request.POST.get("chosen_actor")
    bag = request.session.get("bag", {})

    if selected:
        if quantity > 0:

            bag[item_id]["items_by_selected"][selected] = quantity
            messages.success(
                request,
                f"Updated {ticket.name} quantity "
                f"for {selected} to "
                f'{bag[item_id]["items_by_selected"][selected]}',
            )
            print("updated bag")
            print(bag)
        elif quantity < 0:
            messages.info(request, "Please enter only positive numbers")
        else:
            del bag[item_id]["items_by_selected"][selected]
            messages.success(
                request,
                f"Removed {ticket.name} " f"for {selected} from your bag ",
            )
            print("removed")
            print(bag)
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f"Updated {ticket.name} quantity to \
                {bag[item_id]}.",
            )
            print("working update")
            print(bag)
        elif quantity < 0:
            messages.info(request, "Please enter only positive numbers")
        else:
            del bag[item_id]
            messages.success(request, f"Removed {ticket.name} from your bag.")
    # elif quantity < 0:
    #     messages.info(request, 'Please enter only positive numbers')
    # elif quantity > 0:
    #     bag[item_id] = quantity

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove item from bag"""
    try:
        ticket = get_object_or_404(Ticket, pk=int(item_id))
        selected = None
        if "chosen_actor" in request.POST:
            selected = request.POST.get("chosen_actor")
        bag = request.session.get("bag", {})

        if selected:
            del bag[item_id]["items_by_selected"][selected]
            messages.success(
                request,
                f"Removed {ticket.name} " f" for {selected} from your bag!",
            )
        else:
            del bag[item_id]
            messages.success(request, f"Removed {ticket.name} from your bag.")

        request.session["bag"] = bag
        return redirect(reverse("view_bag"))

    except Exception as error:
        return HttpResponse(status=500, content=error)


def empty_bag(request):
    """Remove all items from bag"""

    bag = request.session.get("bag", {})

    bag.clear()
    messages.success(request, "Removed all items from your bag.")

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))
