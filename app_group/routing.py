from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('chat/<slug:root>', consumers.ChatConsumer.as_asgi()),
]
