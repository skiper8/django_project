from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from catalog.apps import UsersConfig
from users.views import UserUpdateView, RegisterView, EmailActivate

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
    path('activate_email/<uidb64>/<token>/', EmailActivate.as_view(), name='activate_email'),
]
