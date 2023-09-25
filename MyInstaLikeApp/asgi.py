
# your_project/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from your_app import routing  # Import your WebSocket routing

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),
})

