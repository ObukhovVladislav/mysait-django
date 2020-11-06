from django.shortcuts import render

from myapp.models import ProductCategory, Products


def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'myapp/index.html', context)


def catalog(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }
    return render(request, 'myapp/catalog.html', context)


def catalog_page(request, pk):
    items = Products.objects.filter(category_id=pk)
    context = {
        'items': items,
        'page_title': 'страница товаров'
    }
    return render(request, 'myapp/catalog_page.html', context)


def basket(request):
    context = {
        'page_title': 'корзина'
    }
    return render(request, 'myapp/basket.html', context)
