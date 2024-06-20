from rest_framework import serializers

from food_app.models.food import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "description",
            "sub_category",
            "price",
            "image",
            "restaurant",
            "restaurant_name",
            "created_at",
            "updated_at",
        ]
