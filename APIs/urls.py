from django.urls import path, include
from .views import getVideoAPI

# localhost/video
urlpatterns = [
    path("video/", getVideoAPI),
    
]