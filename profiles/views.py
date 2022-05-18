from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """Display the user's profile"""
    try:
        profile = get_object_or_404(UserProfile, user=request.user)

        if request.method == "POST":
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
            else:
                messages.error(
                    request,
                    "Profile could not be  updated. \
                    Please check the form input is valid.",
                )
        else:
            form = UserProfileForm(instance=profile)

        orders = profile.orders.all()

        template = "profiles/profile.html.jinja"
        context = {"form": form, "orders": orders, "on_profile_page": True}

        return render(request, template, context)
    except Http404:
        messages.error(request, "Sorry! You don't have permission to do that!")
        return redirect("home")


@login_required
def order_history(request, order_number):
    """Display the user's order history"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}."
            f"A confirmation email was sent on {order.date}."
        ),
    )

    # re-using the template because it already has the needed layout
    template = "checkout/checkout_success.html.jinja"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
