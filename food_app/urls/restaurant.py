from django.urls import path

from food_app.views.restaurant.viewset import RestaurantViewSet

urlpatterns = [
    path(
        "restaurant/",
        RestaurantViewSet.as_view({"patch": "partial_update", "get": "retrieve"}),
    ),
]
