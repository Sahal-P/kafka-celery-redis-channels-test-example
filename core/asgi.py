import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.conf import settings
from uvicorn import run
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# application = get_asgi_application()

from connect.routing import websocket_urlpatterns
# ws_patters = [
#     path('ws/test/',TestConsumer.as_asgi())
# ]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : URLRouter(websocket_urlpatterns),
})

# if __name__ == "__main__":
#     run(
#         application,
#         host=settings.ALLOWED_HOSTS[0],
#         port=settings.PORT,
#         debug=settings.DEBUG,
#         log_level="info",
#     )
    