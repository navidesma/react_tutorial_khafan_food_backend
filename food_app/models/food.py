from django.db import models

from food_app.models.food_category import FoodSubCategory
from food_app.models.restaurant import Restaurant


class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    sub_category = models.ForeignKey(FoodSubCategory, on_delete=models.PROTECT)
    price = models.PositiveIntegerField()
    image = models.FileField(upload_to="")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "food"
        
        
    @property
    def restaurant_name(self):
        return self.restaurant.name
