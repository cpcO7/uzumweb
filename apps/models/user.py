from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, ManyToManyField

from apps.models.managers import CustomUserManager


class User(AbstractUser):
    phone_number = CharField(max_length=25, unique=True)
    email = EmailField(max_length=255, blank=True, null=True)
    wishes = ManyToManyField('apps.Product', blank=True)
    password = CharField(max_length=150, null=True, blank=True)
    username = None
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
