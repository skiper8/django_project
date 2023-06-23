import random

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator

from config import settings


def generate_code():
    return str(random.randint(10000, 99999))


def send_activate_email(new_user):
    send_mail('код подтверждения', new_user.code,
              settings.EMAIL_HOST_USER,
              [new_user.email],
              fail_silently=False)
