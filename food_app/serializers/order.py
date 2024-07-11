from rest_framework import serializers

from food_app.models.address import Address
from food_app.models.order import Order
from food_app.serializers.address import AddressSerializer
from food_app.serializers.order_item import OrderItemReadSerializer, OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemReadSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = Order
        fields = [
            "id",
            "items",
            "shipping_cost",
            "total_cost",
            "customer",
            "address",
            "deliver_time",
            "is_finished",
            "created_at",
        ]


class OrderSubmitSerializer(serializers.Serializer):
    order_items = OrderItemSerializer(many=True)
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())
