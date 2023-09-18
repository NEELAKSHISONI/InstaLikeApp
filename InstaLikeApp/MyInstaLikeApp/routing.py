from channels.routing import ProtocolTypeRouter, URLRouter
from InstaLikeApp import routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(routing.websocket_urlpatterns),
})
