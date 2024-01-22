from django.urls import path, include
from socialDownloaderApp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('download/', views.downloadMediaView, name='downloadMedia'),
]
