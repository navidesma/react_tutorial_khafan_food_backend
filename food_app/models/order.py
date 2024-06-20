from django.db import models

from food_app.models.food import Food


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    count = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'order'
