from django.db import models

from food_app.models.address import Address
from food_app.models.order import Order
from user_profile.models import Profile


class Cart(models.Model):
    orders = models.ManyToManyField(Order)
    shipping_cost = models.PositiveIntegerField()
    total_cost = models.PositiveIntegerField()
    customer = models.ForeignKey(Profile, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    is_pending = models.BooleanField(default=True)
    finish_time = models.DateTimeField(null=True)
    is_successful = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "cart"

    @property
    def is_finished(self):
        return self.finish_time is not None
