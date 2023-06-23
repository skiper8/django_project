from django.core.mail import send_mail

from config import settings


def send_varify_email(new_user):
    return send_mail(
        subject='Вы прошли регистрацию.',
        message='Пожалуйста подтвердите свою почту пройдя по этой ссылке: ',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[new_user.email]
    )
