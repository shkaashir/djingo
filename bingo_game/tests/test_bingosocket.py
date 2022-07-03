import pytest
from channels.testing import WebsocketCommunicator
from bingo.asgi import application
import json

# Overriding the setting channel layer with InMemorChannelLayer only for testing
# In production the channel layer defined in setting.py will be used.
TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

@pytest.fixture
def communicator():
    communicator = WebsocketCommunicator(
            application=application,
            path="/ws/bingo/"
    )
    return communicator


@pytest.mark.asyncio
class TestBingoPytest:

    async def tests_can_connect_to_the_server(self, settings, communicator)->None:
        """
        Testing whether a client can connect to the server or not.

        Args:
            settings: setting of the project. It is a fixture which is provided py pytest-django 
            communicator: communicator for commuunicating with channels. 
        """
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        
        connected, _ = await communicator.connect()
        
        assert connected is True

        await communicator.disconnect()

    
    async def test_client_can_send_and_receive_message(self, settings, communicator)->None:
        """
        Testing whether a client can send or receive messages.

        Args:
            settings: setting of the project. It is a fixture which is provided py pytest-django 
            communicator: communicator for commuunicating with channels. 
        """

        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS

        await communicator.connect()

        message = {
            'type': 'websocket.send',
            'text': 'This is a test message.',
        }

        print(dir(communicator))

        await communicator.send_json_to(message)

        response = await communicator.receive_from()

        assert response == message["text"]

        await communicator.disconnect()