import random

from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='user_avatar/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False)
    code = models.CharField(verbose_name='код', max_length=255, unique=True, **NULLABLE)

    def save(self, *args, **kwargs):
        self.code = str(random.randint(10000, 99999))
        super(User, self).save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
