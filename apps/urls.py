from django.urls import path

from apps.views import RegisterPageTemplateView, EmailVerificationView, PhoneVerificationView, \
    NewUserPasswordView

urlpatterns = [
    path('register/', RegisterPageTemplateView.as_view(), name='register'),
    path('email-verification/', EmailVerificationView.as_view(), name='email-verification'),
    path('phone-verification/', PhoneVerificationView.as_view(), name='phone-verification'),
    path('new-user/', NewUserPasswordView.as_view(), name='new-user-password'),

]
