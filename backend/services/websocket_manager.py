from fastapi import WebSocket

class ConnectionManager:

    def __init__(self):

        self.active=[]

    async def connect(
        self,
        websocket
    ):

        await websocket.accept()

        self.active.append(
           websocket
        )

    def disconnect(
       self,
       websocket
    ):

       self.active.remove(
         websocket
       )

    async def broadcast(
       self,
       message
    ):

       for user in self.active:

          await user.send_json(
             message
          )

manager=ConnectionManager()