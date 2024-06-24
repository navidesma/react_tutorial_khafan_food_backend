from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from food_app.models.food import Food
from food_app.serializers.food import FoodSerializer
from user_profile.models import UserType

class ListFoodView(ListAPIView):
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        profile = self.request.user.profile
        if profile.type == UserType.RESTAURANT_OWNER.value:
            return Food.objects.filter(restaurant=profile.restaurant)
        
        return Food.objects.all()
    
class ListRestaurantsFood(ListAPIView):
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "restaurant_id"
    
    def get_queryset(self):
        return Food.objects.filter(restaurant_id=self.kwargs.get("restaurant_id"))
