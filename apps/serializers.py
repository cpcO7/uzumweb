from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import DeliveryPoint
from apps.models.shop import Region, District


class LoginSerializer(Serializer):
    phone_number = CharField(max_length=25)


class LoginConfirmSerializer(Serializer):
    phone_number = CharField(max_length=25)
    code = CharField(max_length=5)


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class DistrictModelSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class DeliveryPointModelSerializer(ModelSerializer):
    class Meta:
        model = DeliveryPoint
        fields = ['city', 'location', 'fitting_room', 'working_hour']
