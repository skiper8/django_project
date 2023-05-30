from django.shortcuts import render
from catalog.models import Category, Products
from config.settings import MEDIA_ROOT


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    products_list = Products.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)
