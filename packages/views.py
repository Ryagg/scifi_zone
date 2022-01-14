from django.shortcuts import render, get_object_or_404
from .models import Category, Package

def packages(request):
    """ A view to show all package categories """

    categories = Category.objects.all()


    context = {
        'categories': categories,
    }

    return render(request, 'packages/packages.html', context)


def package_detail(request, categories_id):
    """ A view to show detailed package information """
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=categories_id)
    packages = Package.objects.all()
    package = get_object_or_404(Package, pk=categories_id)
    goodies = package.included.split(',')

    context = {
        'categories': categories,
        'category': category,
        'packages': packages,
        'package': package,
        'goodies': goodies,
    }

    return render(request, 'packages/package_detail.html', context)

