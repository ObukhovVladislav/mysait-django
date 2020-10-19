from django.contrib import admin

from myapp.models import ProductCategories, Products

admin.site.register(ProductCategories)
admin.site.register(Products)