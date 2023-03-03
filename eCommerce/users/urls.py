from django.urls import path, include
from .views import RegisterUserAPIView, LoginUserAPIView

urlpatterns = [
    path('login', LoginUserAPIView.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
]
