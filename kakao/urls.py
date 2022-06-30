from django.urls import path
from . import views

urlpatterns = [
    path('kakaoLogin/', views.kakaoLogin),
    path('kakaoLoginCallback/', views.kakaoLoginCallback),
    path('kakaoLogout/', views.kakaoLogout),
]