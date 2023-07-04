# Generated by Django 4.2.1 on 2023-07-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='code',
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='токен'),
        ),
    ]