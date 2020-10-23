from django.shortcuts import render

from myapp.models import ProductCategories


def index(request):
    return render(request, 'myapp/index.html')


def catalog(request):
    categories = ProductCategories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'myapp/catalog.html', context)


def basket(request):
    return render(request, 'myapp/basket.html')
