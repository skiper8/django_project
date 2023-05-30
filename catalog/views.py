from django.shortcuts import render
from catalog.models import Category, Products
from config.settings import MEDIA_ROOT


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    product_item = Products.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': product_item,
    }
    return render(request, 'catalog/product.html', context)


def home(request):
    products_list = Products.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)
