from django.core.management import BaseCommand

from catalog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **options):
        Blog.objects.all().delete()

        blog_list = [
            {'title': 'Компьютер и что он скрывает внутри', 'text': 'ататтататата', 'is_active': True},
            {'title': 'Робототехника дома', 'text': 'ататтататата', 'is_active': True},
        ]

        blog_objects = []

        for item in blog_list:
            blog_objects.append(Blog(**item))
        Blog.objects.bulk_create(blog_objects)
