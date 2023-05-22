from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog, home

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog),
    path('contacts/', home),
]
