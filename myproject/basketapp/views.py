from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import ProductsBasket
from django.urls import reverse

from myapp.models import Products


def index(request):
    item = ProductsBasket.objects.filter(user=request.user)
    context = {
        'object_list': item,
    }
    return render(request, 'basketapp/basket.html', context)


def add(request, products_id):
    products = Products.objects.get(pk=products_id)
    ProductsBasket.objects.get_or_create(
       user=request.user,
       products=products
    )
    return HttpResponseRedirect(
       reverse('my:catalog_section',
               kwargs={'category_pk': products.category_id})
    )


def remove(request, products_basket_id):
    item = ProductsBasket.objects.get(id=products_basket_id)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
