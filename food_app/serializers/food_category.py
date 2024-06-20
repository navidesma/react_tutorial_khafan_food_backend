from rest_framework import serializers

from food_app.models.food_category import FoodSubCategory, FoodCategory


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = "__all__"


class FoodSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodSubCategory
        fields = "__all__"
