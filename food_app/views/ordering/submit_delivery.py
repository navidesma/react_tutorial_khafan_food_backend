from datetime import datetime
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from food_app.models.order import Order
from user_profile.permissions import IsRestaurantOwnerPermission


class SubmitOrderDeliveryView(UpdateAPIView):
    serializer_class = None
    queryset = Order.objects.all()
    http_method_names = ["put"]
    permission_classes = [IsRestaurantOwnerPermission]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.deliver_time = datetime.now()
        instance.save()

        return Response(status=200)
