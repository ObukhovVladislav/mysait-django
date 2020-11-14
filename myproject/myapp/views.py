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


def catalog_section(request, category_pk):
    items = Products.objects.filter(category_id=category_pk)
    context = {
        'items': items,
        'page_title': 'страница товаров'
    }
    return render(request, 'myapp/catalog_section.html', context)


def product_page(request, product_pk):
    product = Products.objects.get(pk=product_pk)
    context = {
        'product': product,
        'page_title': 'страница товара'
    }
    return render(request, 'myapp/product_page.html', context)


