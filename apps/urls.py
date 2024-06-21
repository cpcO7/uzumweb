from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.views import LoginAPIView, LoginConfirmCreateAPIView, CountryListAPIView, DistrictListAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("login-confirm/", LoginConfirmCreateAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('country/', CountryListAPIView.as_view()),
    path('district/', DistrictListAPIView.as_view()),
]
