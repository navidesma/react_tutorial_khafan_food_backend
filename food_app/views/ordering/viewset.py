from rest_framework import viewsets

from food_app.models.order import Order
from food_app.serializers.order import OrderSerializer
from user_profile.models import UserType
from user_profile.permissions import IsRestaurantOwnerPermission, IsNormalUser


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsRestaurantOwnerPermission | IsNormalUser]

    def get_queryset(self):
        user_profile = self.request.user.profile

        if user_profile.type == UserType.RESTAURANT_OWNER.value:
            return Order.objects.filter(items__food__restaurant=user_profile.restaurant)

        return Order.objects.filter(customer=self.request.user.profile)
