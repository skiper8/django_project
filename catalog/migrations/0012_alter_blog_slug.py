# Generated by Django 4.2.1 on 2023-06-09 07:23

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
