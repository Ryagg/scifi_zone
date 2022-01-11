from django.shortcuts import render, get_object_or_404
from .models import Category, Package

def packages(request):
    """ A view to show all package categories """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'packages/packages.html', context)
