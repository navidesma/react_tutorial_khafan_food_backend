from rest_framework.generics import ListAPIView

from food_app.models.food_category import FoodCategory, FoodSubCategory
from food_app.serializers.food_category import (
    FoodCategorySerializer,
    FoodSubCategorySerializer,
)


class ListCategories(ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
    pagination_class = None


class ListSubCategories(ListAPIView):
    serializer_class = FoodSubCategorySerializer
    pagination_class = None
    lookup_field = "category_id"

    def get_queryset(self):
        return FoodSubCategory.objects.filter(
            category_id=self.kwargs.get("category_id")
        )
