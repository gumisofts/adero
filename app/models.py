from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


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


class Service(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField()
    img = models.ImageField()
