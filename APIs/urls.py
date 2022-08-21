from django.urls import path, include
from .views import getVideoAPI

# localhost/api/hello
urlpatterns = [
    path("hello/", getVideoAPI),
    
]