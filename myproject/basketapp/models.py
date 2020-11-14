from django.contrib.auth.models import User
from django.db import models

from myapp.models import Products


class ProductsBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
