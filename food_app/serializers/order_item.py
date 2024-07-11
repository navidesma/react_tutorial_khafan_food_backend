from rest_framework import serializers

from food_app.models.order_item import OrderItem
from food_app.serializers.food import FoodSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemReadSerializer(serializers.ModelSerializer):
    food = FoodSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "food", "count", "created_at"]
