from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from food_app.models.order import Order
from food_app.serializers.order import OrderSerializer
from user_profile.permissions import IsNormalUser


class SubmitOrderView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsNormalUser]

    def create(self, request, *args, **kwargs):
        request_data = request.data
        request_data["customer"] = request.user.profile
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
