from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from core.mail import *
from django.shortcuts import render


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, first_name):
        user = self.model(email=email, first_name=first_name)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        null=True,
        blank=True,
        editable=False,
    )
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    position = models.ForeignKey(
        "Position", on_delete=models.CASCADE, null=True, blank=True
    )
    pic = models.ImageField(null=True, blank=True)

    github = models.URLField(null=True, blank=True)


class Service(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField()
    img = models.ImageField()


class Position(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    mode = models.CharField(
        max_length=255,
        choices=[("remote", "remote"), ("on-site", "on-site"), ("hybrid", "hybrid")],
    )
    job_type = models.CharField(
        max_length=255,
        choices=[
            ("full-time", "full-time"),
            ("part-time", "part-time"),
            ("contract", "contract"),
            ("internship", "internship"),
        ],
    )
    salary = models.PositiveIntegerField(null=True, blank=True)
    is_open = models.BooleanField(default=True)
    open_from = models.DateField(null=True, blank=True)
    open_to = models.DateField(null=True, blank=True)


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    service = models.ForeignKey(
        "Service", on_delete=models.CASCADE, null=True, blank=True
    )


class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_by = models.ForeignKey(User, on_delete=models.PROTECT)
    catagory = models.CharField(max_length=255, null=True)

    publish = models.BooleanField(default=False)

    def upload_to(self, filename):
        return "blogs/" + filename

    cover_img = models.ImageField(upload_to=upload_to, null=True)


@receiver([post_save], sender=Message)
def send_email_when_message_is_rececived(instance, created, sender, **extra_fields):
    if created:
        send_email_managers()
