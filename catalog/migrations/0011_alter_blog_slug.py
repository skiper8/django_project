# Generated by Django 4.2.1 on 2023-06-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=150, unique=True, verbose_name='slug'),
        ),
    ]
