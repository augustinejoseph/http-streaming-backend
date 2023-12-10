from django.urls import path
from .views import streamerView,streamText

urlpatterns = [
    path('stream-number', streamerView, name='streamer-view'),
    path('stream-text', streamText, name='streamer-view')

]
