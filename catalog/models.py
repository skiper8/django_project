from django.db import models

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
