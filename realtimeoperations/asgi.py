import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import operations.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realtimeoperations.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            operations.routing.websocket_urlpatterns
        )
    ),
})