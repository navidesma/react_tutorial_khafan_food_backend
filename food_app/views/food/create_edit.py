from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

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
    parser_classes = (MultiPartParser, FormParser)

    def check_object_permissions(self, request, obj):
        if obj.restaurant != request.user.profile.restaurant:
            raise PermissionDenied()

    def create(self, request, *args, **kwargs):
        request_data = self.request.data
        request_data["restaurant"] = request.user.profile.restaurant.id
        file_serializer = self.get_serializer(data=request_data)
        file_serializer.is_valid(raise_exception=True)
        self.perform_create(file_serializer)
        headers = self.get_success_headers(file_serializer.data)
        return Response(
            file_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
