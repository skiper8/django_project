from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from catalog.apps import UsersConfig
from users.views import UserUpdateView, UserRegisterView, EmailConfirmationSentView, UserConfirmEmailView, \
    EmailConfirmView, EmailConfirmationFailedView, UserForgotPasswordView, UserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),  # войти
    path('logout/', LogoutView.as_view(), name='logout'),  # выйти
    path('register/', UserRegisterView.as_view(), name='register'),  # регистрация
    path('profile/', UserUpdateView.as_view(), name='profile'),  # профиль
    path('email_confirmation_sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm_email/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email_confirmed/', EmailConfirmView.as_view(), name='email_verified'),
    path('confirm_email_failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
