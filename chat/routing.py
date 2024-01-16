from django.urls import path, re_path
from . import consumers

urlpatterns = [
    re_path(r'ws/chat/', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
