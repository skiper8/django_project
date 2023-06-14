from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductsDetailView, ProductsListView, ContactsListView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView, ProductsUpdateView, ProductsDeleteView, ProductsCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('contacts/', ContactsListView.as_view(), name='contacts_list'),
    path('product/<int:pk>/', ProductsDetailView.as_view(), name='products_detail'),
    path('products/create/', ProductsCreateView.as_view(), name='products_form'),
    path('products/update/<int:pk>/', ProductsUpdateView.as_view(), name='products_update'),
    path('products/delete/<int:pk>/', ProductsDeleteView.as_view(), name='products_delete'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
