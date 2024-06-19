from django.urls import path

from apps.views import MainTemplateView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),
]


