from django.urls import path

from apps.views import LoginAPIView, LoginConfirmCreateAPIView

urlpatterns = [
    path("api/v1/login/", LoginAPIView.as_view()),
    path("api/v1/login-confirm/", LoginConfirmCreateAPIView.as_view())
]
