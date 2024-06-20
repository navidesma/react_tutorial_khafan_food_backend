from rest_framework import serializers

from food_app.models.order import Order


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
