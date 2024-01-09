import json
import asyncio
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

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")
        time_value = data.get("time")

        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

        if time_value:
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_time", "time_value": time_value}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]

        # Send live status to WebSocket
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        print(data)
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))

    async def send_time(self, time_value):
        print(time_value)
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"time": time_value}))


class MatchCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"matchcard_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")


        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        print(data)
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))


class ScheduleCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"schedulecard_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")


        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        print(data)
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))

class RefereesCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"refereescard_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")


        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))

class GoalScorerCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"goalscorer_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")


        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        print(data)
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))

class CardsCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"cardscard_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")


        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        print(data)
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))


class FreeTextCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"freetextcard_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")


        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))

class SwapsCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"swapscard_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")


        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))

class TimeCardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"timecard_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        x = data.get("x")
        y = data.get("y")
        is_live = data.get("isLive")
        component_data = data.get("data")


        if is_live is not None:
            # Handle live status message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_live_status", "isLive": is_live}
            )
        if x is not None and y is not None:
            # Handle drag event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_location", "x": x, "y": y}
            )
        if component_data is not None:
            # Handle data transfer event
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "send_data", "data": component_data}
            )

    async def send_location(self, event):
        x = event["x"]
        y = event["y"]
        await self.send(text_data=json.dumps({"x": x, "y": y}))

    async def send_live_status(self, event):
        is_live = event["isLive"]
        await self.send(text_data=json.dumps({"isLive": is_live}))

    async def send_data(self, data):
        print(data)
        # Handle the additional data as needed
        await self.send(text_data=json.dumps({"data": data}))
