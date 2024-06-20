from rest_framework import serializers
from django.core.validators import RegexValidator

from user_profile.models import UserType, Profile

mobile_number_regex_validator = RegexValidator(regex="^09\d{9}$")


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    type = serializers.ChoiceField(choices=[tag.value for tag in UserType])
    mobile = serializers.CharField(validators=[mobile_number_regex_validator])


class UserSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=[tag.value for tag in UserType])

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "type",
            "mobile",
            "first_name",
            "last_name",
            "full_name",
            "created_at",
            "updated_at",
        ]
