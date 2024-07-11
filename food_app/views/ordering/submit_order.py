from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.db import transaction

from food_app.models.order import Order
from food_app.models.order_item import OrderItem
from food_app.serializers.order import OrderSubmitSerializer
from user_profile.permissions import IsNormalUser


class SubmitOrderView(CreateAPIView):
    serializer_class = OrderSubmitSerializer
    permission_classes = [IsNormalUser]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer = request.user.profile

        order_items: list[OrderItem] = []

        for order_item in serializer.validated_data["order_items"]:
            order_item_instance = OrderItem.objects.create(
                food=order_item.get("food"), count=order_item.get("count")
            )
            order_items.append(order_item_instance)

        shipping_cost = 15000

        food_cost = 0
        for order_item in order_items:
            food_cost += order_item.food.price * order_item.count

        order = Order.objects.create(
            shipping_cost=shipping_cost,
            total_cost=food_cost + shipping_cost,
            customer=customer,
            address=serializer.validated_data.get("address"),
        )

        order.items.set(order_items)

        return Response(status=status.HTTP_201_CREATED)
