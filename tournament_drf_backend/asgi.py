import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chat.routing import websocket_urlpatterns as chat_websocket_urlpatterns
from match.routing import websocket_urlpatterns as match_websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tournament_drf_backend.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(
                chat_websocket_urlpatterns + 
                match_websocket_urlpatterns
            ))
        ),
    }
)