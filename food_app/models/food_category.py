from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'food_category'


class FoodSubCategory(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'food_sub_category'
