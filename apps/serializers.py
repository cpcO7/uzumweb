from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import DeliveryPoint


class LoginSerializer(Serializer):
    phone_number = CharField(max_length=25)


class LoginConfirmSerializer(Serializer):
    phone_number = CharField(max_length=25)
    code = CharField(max_length=5)


class DeliveryPointSerializer(ModelSerializer):
    class Meta:
        model = DeliveryPoint
        fields = ['city', 'location', 'fitting_room', 'working_hour']
