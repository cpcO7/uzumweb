from django.urls import path

from apps.views import MainTemplateView, LoginTemplateView, RegisterTemplateView
from views import RegisterView, ProfileView, EmailVerificationView, PhoneVerificationView, \
    NewUserPasswordView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),

    path('login/', LoginTemplateView.as_view(), name='main_page'),
    path('register/', RegisterTemplateView.as_view(), name='main_page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verification/', EmailVerificationView.as_view(), name='verify'),
    path('phone-verification/', PhoneVerificationView.as_view(), name='verify'),
    path('new-user/', NewUserPasswordView.as_view(), name='verify'),
    path('profile/', ProfileView.as_view(), name='profile'),


]
