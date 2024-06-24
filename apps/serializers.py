from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import DeliveryPoint, Category, Product
from apps.models.shop import Region, District, Wish


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


class CategoryModelSerializer(ModelSerializer):
    children = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'icon', 'children']

    def get_children(self, obj):
        children = obj.get_children()
        return CategoryModelSerializer(children, many=True).data


class WishModelSerializer(ModelSerializer):
    class Meta:
        model = Wish
        fields = "product",


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price']


class WishListModelSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Wish
        fields = "product",
