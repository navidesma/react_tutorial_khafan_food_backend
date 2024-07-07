from django.urls import path
from food_app.views.food.list import ListFoodView, ListRestaurantsFood
from food_app.views.food.create_edit import FoodViewSet, FoodViewSetWithoutPermission

urlpatterns = [
    path("list/", ListFoodView.as_view()),
    path("list/<int:restaurant_id>/", ListRestaurantsFood.as_view()),
    path("create/", FoodViewSet.as_view({"post": "create"})),
    path("<int:pk>/", FoodViewSetWithoutPermission.as_view({"get": "retrieve"})),
    path(
        "update/<int:pk>/",
        FoodViewSet.as_view({"patch": "partial_update", "get": "retrieve"}),
    ),
]
