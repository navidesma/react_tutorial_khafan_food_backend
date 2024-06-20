from food_app.urls.food import urlpatterns as food_urls
from food_app.urls.restaurant import urlpatterns as restaurant_urls
from food_app.urls.address import urlpatterns as address_urls

urlpatterns = food_urls + restaurant_urls + address_urls
