from django.urls import path
from .views import CreatePost , LikePost, UnLikePost

urlpatterns = [
    path("create-post/", CreatePost.as_view()),
    path('like/<int:pk>/', LikePost.as_view()),
    path('unlike/<int:pk>/', UnLikePost.as_view()),
]