import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.models import ChatClub


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # Retrieve existing chat objects for the room
        existing_chats = ChatClub.objects.filter(club_id=self.room_name)

        serialized_chats = [
            {
                'name': chat.user.username,
                'message': chat.message,
                'timestamp': chat.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
            for chat in existing_chats
        ]

        self.accept()

        # Send existing chats to the connected user
        self.send(text_data=json.dumps({
            'type': 'load_chats',
            'chats': serialized_chats
        }))


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        user = text_data_json['user']
        name = text_data_json['name']
        message = text_data_json['message']

        # Create ChatClub object
        chat_club = ChatClub.objects.create(
            user_id=user, 
            message=message,
            club_id=self.room_name, 
        )

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': chat_club.message,
                'name': chat_club.user.username,
                'timestamp': chat_club.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        name = event['name']
        timestamp = event['timestamp']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'name': name,
            'timestamp': timestamp
        }))