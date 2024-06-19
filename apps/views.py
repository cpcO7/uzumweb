from django.views.generic import TemplateView


class MainTemplateView(TemplateView):
    template_name = 'apps/main.html'


class PhoneVerificationView(TemplateView):
    template_name = 'apps/login-register/phone-number-verification.html'


class EmailVerificationView(TemplateView):
    template_name = 'apps/login-register/email-verification.html'


class NewUserPasswordView(TemplateView):
    template_name = 'apps/login-register/new-user-password.html'


