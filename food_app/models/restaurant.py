from django.db import models

from food_app.models.address import Address
from user_profile.models import Profile


class Restaurant(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.PROTECT, editable=False)
    name = models.CharField(max_length=100, null=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "restaurant"

    @property
    def is_creation_completed(self):
        return self.name is not None and self.address is not None
