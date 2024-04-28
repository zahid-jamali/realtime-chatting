from django.urls import path
from . import consumers
ws_urlpatterns=[
    path("ws/socket-server/<str:pk>", consumers.myConsumer.as_asgi()),
]

