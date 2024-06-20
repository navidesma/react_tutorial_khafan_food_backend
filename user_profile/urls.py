from django.urls import path
from user_profile.views.create import CreateUserView
from user_profile.views.retrieve import RetrieveUserOwnProfileView

urlpatterns = [
    path("create/", CreateUserView.as_view()),
    path("get-my-profile/", RetrieveUserOwnProfileView.as_view()),
]
