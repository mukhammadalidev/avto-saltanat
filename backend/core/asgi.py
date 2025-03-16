import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from core.routing import websocket_urlpatterns  # WebSocket marshrutlari

# Django sozlamalarini yuklash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Django'ning ASGI ilovasi
django_asgi_app = get_asgi_application()

# WebSocket va HTTP so‘rovlarini qo‘llab-quvvatlash
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,  # HTTP uchun
        "websocket": AuthMiddlewareStack(  # WebSocket uchun
            URLRouter(websocket_urlpatterns)
        ),
    }
)
