import uuid

from django.db import models
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='название категории')
    category_text = models.CharField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Products(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='название товара')
    product_category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.SET_NULL, null=True)
    product_text = models.TextField(verbose_name='описание товара', **NULLABLE)
    product_image = models.ImageField(upload_to='product_image/', verbose_name='изображение', **NULLABLE)
    product_price = models.IntegerField(verbose_name='цена')
    product_date_create = models.DateField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)
    product_date_edit = models.DateField(verbose_name='дата последнего изменения', auto_now=True, **NULLABLE)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('product_category',)


class Contacts(models.Model):
    contact_text = models.TextField(verbose_name='описание товара', **NULLABLE)

    def __str__(self):
        return 'Контакты'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', unique=True)
    text = models.TextField(verbose_name='содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog_image/', verbose_name='изображение', **NULLABLE)
    date_create = models.DateField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)
    view_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True, verbose_name='публикация')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{uuid.uuid4().hex[:6]}"
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('view_count',)
