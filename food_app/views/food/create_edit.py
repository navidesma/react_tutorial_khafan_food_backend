from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from food_app.models.food import Food
from food_app.serializers.food import FoodSerializer
from user_profile.permissions import IsRestaurantOwnerPermission


class FoodViewSetWithoutPermission(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
    

class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsRestaurantOwnerPermission]

    def check_object_permissions(self, request, obj):
        if obj.restaurant != request.user.profile.restaurant:
            raise PermissionDenied()
