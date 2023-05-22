from django.shortcuts import render


def catalog(request):
    return render(request, 'catalog/catalog.html')


def home(request):
    return render(request, 'home/home.html')
