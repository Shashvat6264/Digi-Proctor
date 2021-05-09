from django.urls import path, include
from . import views


urlpatterns = [
    path('video_feed', views.video_feed, name='video_feed'),
]