from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Название', max_length=128)
    desc = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=200)
    desc = models.TextField('Описание', blank=True)

    # price = models.IntegerField('Цена', default=0)
    is_active = models.BooleanField('Активно', default=True)

    def __str__(self):
        return self.name
