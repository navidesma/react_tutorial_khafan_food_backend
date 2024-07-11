from django.db import models

from food_app.models.address import Address
from food_app.models.order_item import OrderItem
from user_profile.models import Profile


class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    shipping_cost = models.PositiveIntegerField()
    total_cost = models.PositiveIntegerField()
    customer = models.ForeignKey(Profile, on_delete=models.PROTECT, editable=False)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    deliver_time = models.DateTimeField(null=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "order"

    @property
    def is_finished(self):
        return self.deliver_time is not None
