import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['root']

        # Adicione o usuário ao grupo de chat
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Remova o usuário do grupo de chat
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receba a mensagem do usuário e envie para o grupo de chat
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
    

