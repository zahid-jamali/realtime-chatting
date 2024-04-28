from channels.generic.websocket import WebsocketConsumer
from . import models
import json
from . import models
from asgiref.sync import async_to_sync
class myConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name=self.scope["url_route"]['kwargs']["pk"]
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data):
        data=json.loads(text_data)
        if data['type']=="chat":
            obj=models.chattings()
            obj.user=self.scope['user']
            obj.room=models.chat_rooms.objects.get(url= self.room_group_name)
            obj.message=data['message']
            obj.save()

            message=data['message']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat",
                    "message" : message,
                    "user": self.scope["user"].name
                 })

    def chat(self, event):
        print(event)
        msg=event['message']
        user=event['user']
        self.send(json.dumps({"type": "chat", "message": msg, "user":user}))    

