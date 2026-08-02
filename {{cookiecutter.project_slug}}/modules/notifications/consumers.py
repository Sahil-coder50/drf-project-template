import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from rest_framework_simplejwt.tokens import AccessToken
from typing import Optional

class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        query_string = self.scope["query_string"].decode("utf-8")

        access_token = None
        if query_string.startswith("authorization=Bearer"):
            access_token = query_string.split("authorization=Bearer%20")[1]

        user = await self.get_user_from_token(access_token)
        
        self.group_name = f"user_{user}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        logging.info("Sucess")
        await self.accept()

    async def disconnect(self, code: int) -> None:
        logging.info("Error ----->%s", code)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        return await super().disconnect(code)

    async def receive(self, text_data: str | None = None, bytes_data: bytes | None = None) -> None:
        return await super().receive(text_data, bytes_data)

    async def notification(self, event: dict):
        await self.send(text_data=json.dumps({ "message": event.get("message", "")}))

    @database_sync_to_async
    def get_user_from_token(self, access_token) -> Optional[str]:
        try:
            token = AccessToken(access_token)
            return token["user_id"]
        except:
            return None