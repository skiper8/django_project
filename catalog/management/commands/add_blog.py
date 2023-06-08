from django.core.management import BaseCommand

from catalog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **options):
        Blog.objects.all().delete()

        blog_list = [
            {'title': 'Компьютер и что он скрывает внутри', 'slug': 'все о компьютерах', 'text': 'ататтататата',
             'view_count': '0',
             'category': 'Компьютерные комплектующие'},
            {'title': 'Робототехника дома', 'slug': 'действительно ли робот пылесос хочет вас поработить?',
             'text': 'ататтататата', 'view_count': '0',
             'category': 'Бытовая техника'},
        ]

        blog_objects = []

        for item in blog_list:
            blog_objects.append(Blog(**item))
        Blog.objects.bulk_create(blog_objects)
