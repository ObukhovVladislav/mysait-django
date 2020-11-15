import myapp.views as myapp
from django.urls import path

app_name = 'myapp'

urlpatterns = [
    path('', myapp.index, name='index'),
    path('catalog/', myapp.catalog, name='catalog'),

    path('catalog/category/<int:category_pk>/', myapp.catalog_section, name='catalog_section'),

    path('catalog/product/<int:product_pk>/', myapp.product_page, name='product_page'),
]
