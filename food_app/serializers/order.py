from rest_framework import serializers

from food_app.models.address import Address
from food_app.models.order import Order
from food_app.serializers.order_item import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderSubmitSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())
