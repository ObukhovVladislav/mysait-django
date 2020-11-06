import pickle

from django.core.management.base import BaseCommand

from myapp.models import ProductCategory, Products


class Command(BaseCommand):
    help = 'copy of db in file'

    def handle(self, *args, **options):
        categories = ProductCategory.objects.all()
        with open('categories.bin', 'wb') as f:
            pickle.dump(categories, f)

        items = Products.objects.all()
        with open('items.bin', 'wb') as f:
            pickle.dump(items, f)

