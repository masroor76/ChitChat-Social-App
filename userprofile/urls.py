from django.urls import path
from .views import ProfileFeed

urlpatterns = [
    path('', ProfileFeed)
]