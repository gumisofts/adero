from django.core.mail import send_mail
from django.conf import settings


def send_email(subject, message, to):
    return send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to],
        fail_silently=False,
    )


def send_email_html(subject, html_message, to):
    return send_mail(
        subject=subject,
        message="",
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to],
        fail_silently=False,
    )


def send_email_admins(subject, html_message):
    return send_mail(
        subject=subject,
        message="",
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email for name, email in settings.ADMINS],
        fail_silently=False,
    )


def send_email_managers(subject, html_message):
    return send_mail(
        subject=subject,
        message="",
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email for name, email in settings.MANAGERS],
        fail_silently=False,
    )
