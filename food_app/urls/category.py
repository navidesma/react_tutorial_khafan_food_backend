from django.urls import path
from food_app.views.category import ListCategories, ListSubCategories

urlpatterns = [
    path("category/", ListCategories.as_view()),
    path("sub-category/<int:category_id>/", ListSubCategories.as_view()),
]
