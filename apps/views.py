from random import randint

from django.core.cache import cache
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response

from apps.models import User, DeliveryPoint
from apps.serializers import DeliveryPointSerializer, LoginSerializer, LoginConfirmSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from apps.filters import DistrictFilter
from apps.models import User
from apps.models.shop import Country, District
from apps.serializers import LoginSerializer, LoginConfirmSerializer, CountrySerializer, DistrictSerializer



class DeliveryPointByCityView(ListAPIView):
    queryset = DeliveryPoint.objects.all()
    serializer_class = DeliveryPointSerializer

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
    serializer_class = LoginSerializer

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
    model = User
    serializer_class = LoginConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            conf_code = serializer.validated_data['code']
            phone_number = serializer.validated_data['phone_number']
            if cache.get(conf_code) == phone_number:
                user, created = User.objects.get_or_create(phone_number=phone_number,
                                                           defaults={'phone_number': phone_number})
                # return Response({"message": "Successfully login"})

                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Confirmation successful',
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                })

            return Response({"message": "Invalid or expired code"})

        return Response(serializer.errors)


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filterset = DistrictFilter,
    filter_backends = DjangoFilterBackend,

