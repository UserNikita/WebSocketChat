from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatEvents:
    """Типы событий чата"""
    MESSAGE = 'chat_message'
    JOIN = 'chat_join'
    LEAVE = 'chat_leave'


class ChatConsumer(AsyncJsonWebsocketConsumer):
    """Класс управляющий чатом"""
    GROUP_NAME = 'group'

    async def connect(self):
        if self.scope['user'].is_anonymous:
            await self.close()
        else:
            await self.accept()
            await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
            message = {
                'type': ChatEvents.JOIN,
                'sender': self.scope['user'].username,
            }
            await self.channel_layer.group_send(self.GROUP_NAME, message)

    async def disconnect(self, code):
        if not self.scope['user'].is_anonymous:
            message = {
                'type': ChatEvents.LEAVE,
                'sender': self.scope['user'].username,
            }
            await self.channel_layer.group_send(self.GROUP_NAME, message)

    async def receive_json(self, content, **kwargs):
        message = {
            'type': ChatEvents.MESSAGE,
            'text': content['text'],
            'sender': self.scope['user'].username,
        }
        await self.channel_layer.group_send(self.GROUP_NAME, message)

    async def chat_join(self, event):
        """Вызывается при присоединении нового пользователя"""
        await self.send_json({
            'type': 'join',
            'sender': event['sender'],
        })

    async def chat_leave(self, event):
        """Вызывается, если пользователь покинул чат"""
        await self.send_json({
            'type': 'leave',
            'sender': event['sender'],
        })

    async def chat_message(self, event):
        """Вызывается, если пользователь отправил сообщение"""
        await self.send_json({
            'type': 'message',
            'message': event['text'],
            'sender': event['sender'],
        })
