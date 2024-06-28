from random import randint

from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.filters import DistrictFilter
from apps.models import User, DeliveryPoint, Region, District, Category, Product
from apps.models.shop import Wish
from apps.serializers import DeliveryPointModelSerializer, LoginSerializer, LoginConfirmSerializer, \
    RegionModelSerializer, \
    DistrictModelSerializer, WishModelSerializer, CategoryModelSerializer, \
    ProductModelSerializer, WishListModelSerializer


class DeliveryPointByCityView(ListAPIView):
    queryset = DeliveryPoint.objects.all()
    serializer_class = DeliveryPointModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        grouped_data = {}

        for dp in queryset:
            city = dp.city
            dp_data = self.get_serializer(dp).data
            if city not in grouped_data:
                grouped_data[city] = []
            grouped_data[city].append(dp_data)

        return Response(grouped_data)


class LoginAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = AllowAny,

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            if phone_number.startswith("+998") and len(phone_number) == 13 and phone_number[1:].isdigit():
                conf_code = randint(10000, 99999)
                cache.set(str(conf_code), phone_number, 60)

                return Response({"confirmation_code": conf_code})
            return Response({"error": "Invalid phone number"})

        return Response(serializer.errors)


class LoginConfirmCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginConfirmSerializer
    permission_classes = AllowAny,

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            conf_code = serializer.validated_data['code']
            phone_number = serializer.validated_data['phone_number']
            if cache.get(conf_code) == phone_number:
                user, created = User.objects.get_or_create(phone_number=phone_number,
                                                           defaults={'phone_number': phone_number})
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'OK',
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                })

            return Response({"message": "Invalid or expired code"})

        return Response(serializer.errors)


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictModelSerializer
    filterset_class = DistrictFilter
    filter_backends = DjangoFilterBackend,


class WishListCreateAPIView(ListCreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(id__in=list(request.user.wish_set.values_list('product_id', flat=True)))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductModelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product = get_object_or_404(Product.objects.all(), pk=product_id)
        obj, created = self.get_queryset().get_or_create(user=request.user, product=product)
        if created:
            return Response({'msg': 'successfully created'}, status.HTTP_201_CREATED)
        obj.delete()
        return Response({'msg': 'successfully deleted'}, status.HTTP_204_NO_CONTENT)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = AllowAny,


class WishCreateDeleteAPIView(CreateAPIView):
    serializer_class = WishModelSerializer

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        user = self.request.user

        existing_wish = Wish.objects.filter(user=user, product_id=product_id).first()

        if existing_wish:
            existing_wish.delete()
        else:
            serializer.save(user=user)


class WishListApiView(ListAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishListModelSerializer
    permission_classes = AllowAny,
