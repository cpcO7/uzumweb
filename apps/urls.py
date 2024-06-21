from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.views import RegionListAPIView, DistrictListAPIView, DeliveryPointByCityView, LoginAPIView, \
    LoginConfirmCreateAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("login-confirm/", LoginConfirmCreateAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('region/', RegionListAPIView.as_view()),
    path('district/', DistrictListAPIView.as_view()),
    path("login-confirm/", LoginConfirmCreateAPIView.as_view()),
    path('delivery-points-by-city/', DeliveryPointByCityView.as_view(), name='delivery-points-by-city'),
]
