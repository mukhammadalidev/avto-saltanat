import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("news_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("news_updates", self.channel_name)

    async def send_news_update(self, event):
        news_data = event["news"]
        await self.send(text_data=json.dumps(news_data))
