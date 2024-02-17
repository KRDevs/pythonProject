from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

MALE, FEMALE = ("male", "female")


class UserRoleChoice(models.TextChoices):
    ORDINARY_USER = "ordinary_user"
    MANAGER = "manager"
    SUPER_ADMIN = "super_admin"


class AuthTypeChoice(models.TextChoices):
    VIA_EMAIL = "via_email"
    VIA_PHONE = "via_phone"
    VIA_USERNAME = "via_username"


class SexChoice(models.TextChoices):
    MALE = "male"
    FEMALE = "female"


class User(AbstractUser):
    _validate_phone = RegexValidator(
        regex=r"^998[0-9]{9}$",
        message="O'zbekiston raqamini kiriting! M-n:998975132525"
    )
    userRoles = models.CharField(max_length=31, choices=UserRoleChoice.choices, default=UserRoleChoice.ORDINARY_USER)
    autType = models.CharField(max_length=31, choices=AuthTypeChoice.choices, default=AuthTypeChoice.VIA_USERNAME)
    sex = models.CharField(max_length=15, choices=SexChoice.choices, null=True)
    email = models.EmailField(null=True, unique=True)
    phone_number = models.CharField(max_length=13, null=True, unique=True, validators=[_validate_phone])
    bio = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username
