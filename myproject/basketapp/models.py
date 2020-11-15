from django.contrib.auth.models import User
from django.db import models

from myapp.models import Products


class ProductsBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.added.strftime("%Y.%m.%d %H:%M")}: {self.products.name}'

    def to_html(self):
        return f'{self.added.strftime("%Y.%m.%d %H:%M")}: <b>{self.products.name}</b>'

