from django.urls import path

from food_app.views.ordering.submit_order import SubmitOrderView

urlpatterns = [
    path("order/submit", SubmitOrderView.as_view()),
]
