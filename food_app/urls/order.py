from django.urls import path

from food_app.views.ordering.submit_order import SubmitOrderView
from food_app.views.ordering.viewset import OrderViewSet

urlpatterns = [
    path("order/submit/", SubmitOrderView.as_view()),
    path("order/list/", OrderViewSet.as_view({"get": "list"})),
]
