from rest_framework import serializers

from food_app.models.restaurant import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "owner",
            "address",
            "created_at",
            "updated_at",
            "is_creation_completed",
        ]
