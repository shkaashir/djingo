from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
import json
from utils.random_bingo_number import generate_bingo_numbers
import random


class BingoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Connecting websocket and handshake about to complete.")

        await self.channel_layer.group_add(
            'bingo',
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })

        await self.send({
            "type": "websocket.send",
            "text": json.dumps(generate_bingo_numbers())
        })

        
    async def websocket_receive(self, event):
        await self.channel_layer.group_send(
            'bingo',
            {
                "type": "moderator.random",
                "text": random.randint(1, 75)
            }
        )

    async def moderator_random(self, event):
        print("Got an event for moderator.")
        await self.send({
            "type": "websocket.send",
            "text": str(event["text"])
        })
        
    async def websocket_disconnect(self, event):
        print("Disconnected either from server or client.")
        raise StopConsumer()