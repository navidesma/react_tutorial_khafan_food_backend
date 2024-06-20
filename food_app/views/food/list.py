from rest_framework.generics import ListAPIView

from food_app.models.food import Food
from food_app.serializers.food import FoodSerializer


class ListFoodView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
