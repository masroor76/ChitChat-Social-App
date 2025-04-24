from django.urls import path
from .views import LoginView,RegisterView,LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("register/", RegisterView.as_view())
]