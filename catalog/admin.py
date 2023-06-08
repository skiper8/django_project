from django.contrib import admin

from catalog.models import Category, Products, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name', 'category_text')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category',)
    search_fields = ('product_name', 'product_text',)
    list_filter = ('product_category',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'view_count', 'image')
    search_fields = ('title',)
    list_filter = ('view_count', 'slug',)
