from channels.routing import route
from .consumers import websocket_receive

channel_routing = [
    route("websocket.receive", websocket_receive, path=r"^/sockets/chat/"),
]
