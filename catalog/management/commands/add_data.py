from django.core.management import BaseCommand

from catalog.models import Category, Products


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Products.objects.all().delete()

        category_list = [
            {'category_name': 'Бытовая техника', 'category_text': ''},
            {'category_name': 'Садовые принадлежности', 'category_text': ''},
            {'category_name': 'Компьютерные комплектующие', 'category_text': ''}
        ]
        product_list = [
            {'product_name': 'Пылесос', 'product_category': '', 'product_price': '10000'},
            {'product_name': 'RTX 5090', 'product_category': '', 'product_price': '500000'},
            {'product_name': 'Шланг садовый', 'product_category': '', 'product_price': '1500'},
            {'product_name': 'Intel i9', 'product_category': '', 'product_price': '90000'}
        ]

        category_objects = []
        product_objects = []

        for item in category_list:
            category_objects.append(Category(**item))
        Category.objects.bulk_create(category_objects)

        for item in product_list:
            product_objects.append(Products(**item))
        Products.objects.bulk_create(product_objects)
