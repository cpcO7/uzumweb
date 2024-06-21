from django.urls import path

from apps.views import DeliveryPointByCityView, LoginAPIView, LoginConfirmCreateAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("login-confirm/", LoginConfirmCreateAPIView.as_view()),
    path('api/delivery-points-by-city/', DeliveryPointByCityView.as_view(), name='delivery-points-by-city'),
]
