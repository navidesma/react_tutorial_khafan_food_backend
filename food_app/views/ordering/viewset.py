from rest_framework import viewsets

from food_app.models.order import Order
from food_app.serializers.order import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.profile)
