from rest_framework.fields import CharField, SerializerMethodField, CurrentUserDefault, HiddenField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import DeliveryPoint, Category, Product, SearchHistory, Region, District, Wish


class LoginSerializer(Serializer):
    phone_number = CharField(max_length=25)


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class DistrictModelSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class LoginConfirmSerializer(Serializer):
    phone_number = CharField(max_length=25)
    code = CharField(max_length=5)


class DeliveryPointModelSerializer(ModelSerializer):
    class Meta:
        model = DeliveryPoint
        fields = ['city', 'location', 'fitting_room', 'working_hour']


class CategoryModelSerializer(ModelSerializer):
    children = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'icon', 'children']

    def get_children(self, obj: Category):
        children = obj.get_children()
        return CategoryModelSerializer(children, many=True).data


class SubCategoryModelSerializer(ModelSerializer):
    children = SerializerMethodField()
    product_count = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'product_count', 'icon', 'children']

    def get_product_count(self, obj: Category):
        return obj.products.count()

    def get_children(self, obj):
        children = obj.get_children()
        return CategoryModelSerializer(children, many=True).data


class WishModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Wish
        fields = 'product', 'user'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price']


class WishListModelSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Wish
        fields = "product",


class SearchHistoryModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = SearchHistory
        fields = "keyword", "user",
