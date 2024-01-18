from django.urls import path, include
from socialDownloaderApp import views
import debug_toolbar


urlpatterns = [
    path('', views.home, name='home'),
    path('download/', views.downloadMediaView, name='downloadMedia'),
    path('__debug__/', include(debug_toolbar.urls))
]
