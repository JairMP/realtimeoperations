from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/operacion/(?P<room_name>\w+)/$', consumers.OperacionConsumer.as_asgi()),
]