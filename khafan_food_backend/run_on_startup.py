from django.db import connection, transaction
from food_app.models.food_category import FoodCategory, FoodSubCategory


def get_table_names(cursor=None) -> list:
    try:
        if not cursor:
            cursor = connection.cursor()
        if not cursor:
            raise Exception
        table_names = connection.introspection.get_table_list(cursor)
    except:
        raise Exception("unable to determine if the table '%s' exists")
    else:
        return table_names


@transaction.atomic
def run_on_start_up():
    if (
        any(obj.name == "food_category" for obj in get_table_names())
        and len(FoodSubCategory.objects.all()) == 0
    ):
        sonati = FoodCategory.objects.create(name="سنتی")
        FoodSubCategory.objects.create(name="کبابی", category=sonati)
        FoodSubCategory.objects.create(name="آش و آبگوشت", category=sonati)
        FoodSubCategory.objects.create(name="خورش", category=sonati)

        fast_food = FoodCategory.objects.create(name="فست فود")
        FoodSubCategory.objects.create(name="پیتزا", category=fast_food)
        FoodSubCategory.objects.create(name="ساندویچ", category=fast_food)
        FoodSubCategory.objects.create(name="سوخاری", category=fast_food)

        salem = FoodCategory.objects.create(name="غذای سالم")
        FoodSubCategory.objects.create(name="سالاد", category=salem)
        FoodSubCategory.objects.create(name="رژیمی", category=salem)

        sard = FoodCategory.objects.create(name="غذای سرد")
        FoodSubCategory.objects.create(name="ساندویچ", category=sard)
        FoodSubCategory.objects.create(name="سالاد", category=sard)

        mokhalafat = FoodCategory.objects.create(name="مخلفات")
        FoodSubCategory.objects.create(name="نوشیدنی", category=mokhalafat)
        FoodSubCategory.objects.create(name="سالاد", category=mokhalafat)
