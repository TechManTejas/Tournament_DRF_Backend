import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ScoreCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"scorecard_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")

        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        elif x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )

    # Receive message from room group
    async def send_location(self, event):
        x = event["x"]
        y = event["y"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    # Receive live status from room group
    async def send_live_status(self, event):
        is_live = event["isLive"]

        # Send live status to WebSocket
        await self.send(text_data=json.dumps({"isLive": is_live}))
