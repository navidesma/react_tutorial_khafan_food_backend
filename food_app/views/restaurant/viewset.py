from rest_framework import viewsets

from food_app.models.restaurant import Restaurant
from food_app.serializers.restaurant import RestaurantSerializer
from user_profile.permissions import IsRestaurantOwnerPermission


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsRestaurantOwnerPermission]
    lookup_field = None

    def get_object(self):
        return self.request.user.profile.restaurant
