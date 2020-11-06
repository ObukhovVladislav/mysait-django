import pickle

from django.core.management.base import BaseCommand

from myapp.models import ProductCategory, Products


class Command(BaseCommand):
    help = 'copy of db in file'

    def handle(self, *args, **options):
        with open('categories.bin', 'rb') as f:
            categories = pickle.load(f)

        # for item in categories
        #     ProductCategory.objects.create(
        #         name=item.name,
        #     )


        with open('items.bin', 'rb') as f:
            items = pickle.load(f)
        for item in items:
            Products.objects.create(
                name=item.name,
            )

