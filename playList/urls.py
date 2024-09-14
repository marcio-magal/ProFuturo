from django.urls import path
from . import views
urlpatterns = [
    path('', views.playList),
    path('videoplayer/', views.videoPlayer)
]
