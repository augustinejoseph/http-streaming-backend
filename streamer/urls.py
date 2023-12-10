from django.urls import path
from .views import streamerView

urlpatterns = [
    path('stream', streamerView, name='streamer-view')
]
