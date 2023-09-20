from channels.routing import ProtocolTypeRouter, URLRouter
from MyInstaLikeApp import routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(routing.websocket_urlpatterns),
})
