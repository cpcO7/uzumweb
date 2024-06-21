from random import randint

from django.core.cache import cache
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView
from rest_framework.response import Response

from apps.models import User, DeliveryPoint
from apps.serializers import DeliveryPointSerializer, LoginSerializer, LoginConfirmSerializer


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
                User.objects.get_or_create(phone_number=phone_number, defaults={'phone_number': phone_number})
                return Response({"message": "Successfully login"})

            return Response({"message": "Invalid or expired code"})

        return Response(serializer.errors)
