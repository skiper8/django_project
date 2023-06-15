from django.contrib.auth.views import LoginView
from django.urls import path

from catalog.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
]
