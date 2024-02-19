from django.contrib.auth.models import AbstractUser,UserManager
from django.core.validators import RegexValidator
from django.db import models
import random
from datetime import datetime,timedelta


class UserRoleChoice(models.TextChoices):
    ORDINARY_USER = "ORDINARY_USER"
    MANAGER = "MANAGER"
    SUPER_ADMIN = "SUPER_ADMIN"


class AuthTypeChoice(models.TextChoices):
    VIA_EMAIL = "VIA_EMAIL"
    VIA_PHONE = "VIA_PHONE"
    VIA_USERNAME = "VIA_USERNAME"


class SexChoice(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"
class TypeChoice(models.TextChoices):
    VIA_EMAIL = "VIA_EMAIL"
    VIA_PHONE = "VIA_PHONE"

phoneExpire=2
emailExpire=5

class UserConfirmation(models.Model):
    code=models.CharField(max_length=4)
    user=models.ForeignKey('users.User',on_delete=models.CASCADE)
    verifyType=models.CharField(max_length=31,choices=TypeChoice.choices,null=True)
    expirationTime=models.DateTimeField(null=True)
    isConfirmed=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.__str__())

    def save(self,*args,**kwargs):
        if not self.pk:
            if self.verifyType==VIA_EMAIL:
                self.expirationTime=datetime.now()+timedelta(minutes=emailExpire)
            else:
                self.expirationTime=datetime.now()+timedelta(minutes=phoneExpire)
        super(UserConfirmation,self).save(*args,**kwargs)

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

    objects=UserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def create_verify_code(self,verify_type):
        code="".join([str(random.randint(0,100)%10) for _ in range(4)])
        UserConfirmation.objects.create(
            user_id=self.id,
            verifyType=verifyType,
            code=code
            )
        return code

