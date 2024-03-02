import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from simple_app.routing import websocket_urlpatterns
import simple_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_proj.settings')

application = ProtocolTypeRouter({ 
  "http": get_asgi_application(), 
  "websocket": AuthMiddlewareStack( 
        URLRouter( 
            simple_app.routing.websocket_urlpatterns 
        ) 
    ), 
}) 
