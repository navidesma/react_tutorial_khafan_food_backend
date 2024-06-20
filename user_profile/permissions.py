from rest_framework.permissions import BasePermission
from user_profile.models import UserType


class IsRestaurantOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.profile.type == UserType.RESTAURANT_OWNER.value

        return False


class IsNormalUser(BasePermission):
    class IsRestaurantOwnerPermission(BasePermission):
        def has_permission(self, request, view):
            if request.user and request.user.is_authenticated:
                return request.user.profile.type == UserType.NORMAL_USER.value

            return False
