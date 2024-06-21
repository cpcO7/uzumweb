from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import DeliveryPoint
from .serializers import DeliveryPointSerializer


class DeliveryPointByCityView(ListAPIView):
    queryset = DeliveryPoint.objects.all()
    serializer_class = DeliveryPointSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        grouped_data = {}

        for dp in queryset:
            city = dp.city
            dp_data = self.get_serializer(dp).data
            if city not in grouped_data:
                grouped_data[city] = []
            grouped_data[city].append(dp_data)

        return Response(grouped_data)
