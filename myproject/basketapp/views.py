from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import ProductsBasket
from django.urls import reverse

from myapp.models import Products


def index(request):
    return render(request, 'basketapp/basket.html')


def add(request, products_id):
    products = Products.objects.get(pk=products_id)
    ProductsBasket.objects.get_or_create(
       user=request.user,
       # products_id=products_id
       products=products
    )
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(
       reverse('my:catalog_section',
               kwargs={'category_pk': products.category_id })
    )


