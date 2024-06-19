from django.urls import path

from apps.views import MainTemplateView, BoxMenuTemplateView
from apps.views import RegisterPageTemplateView, EmailVerificationView, PhoneVerificationView, \
    NewUserPasswordView, MainPageView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),
    path('box-menu', BoxMenuTemplateView.as_view(), name='box_page'),
    path('', MainPageView.as_view(), name='main-page'),
    path('register/', RegisterPageTemplateView.as_view(), name='register'),
    path('email-verification/', EmailVerificationView.as_view(), name='email-verification'),
    path('phone-verification/', PhoneVerificationView.as_view(), name='phone-verification'),
    path('new-user/', NewUserPasswordView.as_view(), name='new-user-password'),
]


