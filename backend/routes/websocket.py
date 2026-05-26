from fastapi import APIRouter
from fastapi import WebSocket

from app.services.websocket_service import manager

router=APIRouter()

@router.websocket("/ws")

async def websocket_endpoint(
 websocket:WebSocket
):

 await manager.connect(
    websocket
 )

 try:

   while True:

      data=await websocket.receive_json()

      await manager.broadcast(
         data
      )

 except:

   manager.disconnect(
      websocket
   )