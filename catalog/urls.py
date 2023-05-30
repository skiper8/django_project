from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('produkt/<int:pk>/', product, name='product'),
]

