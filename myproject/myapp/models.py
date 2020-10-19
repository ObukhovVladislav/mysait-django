from django.db import models


class ProductCategories(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ComputersLaptopsAndSoftware(models.Model):
    category = models.ForeignKey(ProductCategories,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)


class HouseholdAppliance(models.Model):
    category = models.ForeignKey(ProductCategories,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)