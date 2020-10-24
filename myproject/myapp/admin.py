from django.contrib import admin

from myapp.models import ProductCategory, Products

admin.site.register(ProductCategory)
admin.site.register(Products)
