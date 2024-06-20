from django.urls import path

from apps.views import LoginAPIView, LoginConfirmCreateAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("login-confirm/", LoginConfirmCreateAPIView.as_view())
]
