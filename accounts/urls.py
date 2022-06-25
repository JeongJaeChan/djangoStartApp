from django.urls import path

from accounts.models import User
from accounts.views import UserViewSet

urlpatterns = [
    path("v1/user", UserViewSet.as_view({"get": "list"}), name="User"),
    # path("v1/users/<int:music_num>", User.as_view({"get": "list"}), name="music"),
]