from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class UserType(Enum):
    RESTAURANT_OWNER = "RESTAURANT_OWNER"
    NORMAL_USER = "NORMAL_USER"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    mobile = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    type = models.CharField(
        max_length=64, choices=[(tag, tag.value) for tag in UserType]
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "profile"

    @property
    def username(self):
        return self.user.username

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
