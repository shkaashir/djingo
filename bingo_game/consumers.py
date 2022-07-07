from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
import json
from utils.random_bingo_number import generate_bingo_numbers
import random


class BingoConsumer(AsyncConsumer):

    bingo_initial_number: str = str(random.randint(1, 75))

    async def websocket_connect(self, event):

        print("Connecting websocket and handshake about to complete.")

        await self.channel_layer.group_add(
            'bingo',
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })

        message = {
            "bingo_numbers": generate_bingo_numbers(),
            "intial_number": self.bingo_initial_number
        }

        await self.channel_layer.group_send('bingo', {
            "type": "bingo.number",
            "text": json.dumps(message)
        })


    async def bingo_number(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })
        
        
    async def websocket_disconnect(self, event):
        print("Disconnected either from server or client.")
        raise StopConsumer()