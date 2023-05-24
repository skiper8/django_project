from django.contrib import admin

from catalog.models import Category, Products


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name', 'category_text')


@admin.register(Products)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category',)
    search_fields = ('product_name', 'product_text',)
    list_filter = ('product_category',)
