from django.urls import path

from food_app.views.address.viewset import AddressViewSet

urlpatterns = [
    path("address/", AddressViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "address/<int:pk>/",
        AddressViewSet.as_view({"patch": "partial_update", "get": "retrieve"}),
    ),
]
