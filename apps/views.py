
from django.views.generic import TemplateView, ListView

from apps.models import ProductImage


class RegisterPageTemplateView(TemplateView):
    template_name = 'apps/login-register/register.html'


class PhoneVerificationView(TemplateView):
    template_name = 'apps/login-register/phone-number-verification.html'


class EmailVerificationView(TemplateView):
    template_name = 'apps/login-register/email-verification.html'


class NewUserPasswordView(TemplateView):
    template_name = 'apps/login-register/new-user-password.html'


class MainPageView(ListView):
    model = ProductImage
    template_name = 'apps/main.html'
    context_object_name = 'products'
