from django.urls import path

from apps.views import DeliveryPointByCityView

urlpatterns = [
    path('api/delivery-points-by-city/', DeliveryPointByCityView.as_view(), name='delivery-points-by-city'),
]
