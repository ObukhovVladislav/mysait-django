from django.shortcuts import render

from myapp.models import ProductCategory, Products


def index(request):
    return render(request, 'myapp/index.html')


def catalog(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }
    return render(request, 'myapp/catalog.html', context)


def basket(request):
    return render(request, 'myapp/basket.html')


def catalog_page(request, pk):
    items = Products.objects.filter(category_id=pk)
    context = {
        'items': items,
        'page_title': 'страница каталога'
    }
    return render(request, 'myapp/catalog_page.html', context)
