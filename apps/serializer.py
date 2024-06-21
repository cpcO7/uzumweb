from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import User


class LoginSerializer(Serializer):
    phone_number = CharField(max_length=25)


class LoginConfirmSerializer(Serializer):
    phone_number = CharField(max_length=25)
    code = CharField(max_length=5)
