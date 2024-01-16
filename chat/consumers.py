import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class ChatConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.room_name = "default_room"
        self.room_group_name = f"chat_{self.room_name}"

        print("--------CONNECTED -----------")

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        # Send welcome message to the client
        self.send_json({
            "type": "chat.message",
            "message": "Hey there! You've successfully connected!",
        })

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send the received message to the room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': f"{self.scope['user']} says: {message}",
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send_json({
            'type': 'chat.message',
            'message': message,
        })
