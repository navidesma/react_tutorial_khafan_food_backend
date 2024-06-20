from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.response import Response

from food_app.models.restaurant import Restaurant
from user_profile.models import Profile, UserType
from user_profile.serializers import CreateUserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        username = data.get("username")

        if User.objects.filter(username=username).exists():
            raise ValidationError({"detail": "این نام کاربری قابل استفاده نیست"})

        user = User.objects.create(username=username)

        user.set_password(data.get("password"))

        user.save()

        user_type = data.get("type")

        profile = Profile.objects.create(
            user=user,
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            type=user_type,
            mobile=data.get("mobile"),
        )

        if user_type == UserType.RESTAURANT_OWNER.value:
            Restaurant.objects.create(owner=profile)

        return Response(status=201)
