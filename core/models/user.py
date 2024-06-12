from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, ManyToManyField


class User(AbstractUser):
    phone_number = CharField(max_length=25)
    email = EmailField(max_length=255, blank=True, null=True)
    wishes = ManyToManyField('core.Product', blank=True)
