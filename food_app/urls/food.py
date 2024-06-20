from django.urls import path
from food_app.views.food.list import ListFoodView

urlpatterns = [path("list/", ListFoodView.as_view())]
