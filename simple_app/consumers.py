# simple_app/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Add the connected client to a specific group
        await self.channel_layer.group_add(
            'display_clear_group',
            self.channel_name
        )

    async def disconnect(self, close_code):
        # Remove the client from the group when disconnected
        await self.channel_layer.group_discard(
            'display_clear_group',
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']

        if message_type == 'display':
            # Broadcast the display message to all clients in the group
            await self.channel_layer.group_send(
                'display_clear_group',
                {
                    'type': 'display_message',
                    'message': 'hi',
                }
            )
        elif message_type == 'clear':
            # Broadcast the clear message to all clients in the group
            await self.channel_layer.group_send(
                'display_clear_group',
                {
                    'type': 'clear_message',
                }
            )

    async def display_message(self, event):
        # Send the display message to the WebSocket
        await self.send(text_data=json.dumps({
            'type': 'display',
            'message': event['message']
        }))

    async def clear_message(self, event):
        # Send the clear message to the WebSocket
        await self.send(text_data=json.dumps({
            'type': 'clear'
        }))
