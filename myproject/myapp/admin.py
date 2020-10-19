from django.contrib import admin

from myapp.models import ProductCategories, ComputersLaptopsAndSoftware, HouseholdAppliance


admin.site.register(ProductCategories)
admin.site.register(ComputersLaptopsAndSoftware)
admin.site.register(HouseholdAppliance)