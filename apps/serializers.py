from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import DeliveryPoint
from apps.models.shop import Country, District


class LoginSerializer(Serializer):
    phone_number = CharField(max_length=25)


class LoginConfirmSerializer(Serializer):
    phone_number = CharField(max_length=25)
    code = CharField(max_length=5)


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class DeliveryPointSerializer(ModelSerializer):
    class Meta:
        model = DeliveryPoint
        fields = ['city', 'location', 'fitting_room', 'working_hour']
