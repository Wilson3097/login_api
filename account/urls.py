from django.urls import path
from .views import registration_view, UserLoginAPIView
urlpatterns = [
    path("register/", registration_view, name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login")
]
