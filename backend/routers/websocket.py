from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from websocket.manager import manager
from services.user_service import user_exists, set_user_online_status
from services.message_service import save_chat_message
from schemas.message import ChatMessageCreate

router = APIRouter()


def serialize_message(message):
    return {
        "id": message.id,
        "content": message.content,
        "sender": message.sender,
        "receiver": message.receiver,
        "color": message.color,
        "timeStamp": message.time_stamp.isoformat() if message.time_stamp else None,
        "messageType": message.message_type,
    }


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            destination = data.get("destination")
            body = data.get("body") if isinstance(data.get("body"), dict) else data

            if destination == "/app/chat.addUser":
                username = body.get("sender")
                if username and user_exists(db, username):
                    set_user_online_status(db, username, True)
                    manager.register_user(username, websocket)

                    payload = ChatMessageCreate(
                        sender=username,
                        content=body.get("content", ""),
                        messageType=body.get("messageType", "JOIN"),
                        timeStamp=body.get("timeStamp"),
                    )
                    message = save_chat_message(db, payload)
                    await manager.broadcast(serialize_message(message))

            elif destination == "/app/chat.sendMessage":
                payload = ChatMessageCreate(
                    sender=body.get("sender"),
                    content=body.get("content", ""),
                    messageType=body.get("messageType", "CHAT"),
                    timeStamp=body.get("timeStamp"),
                )
                if payload.sender and user_exists(db, payload.sender):
                    message = save_chat_message(db, payload)
                    await manager.broadcast(serialize_message(message))

            elif destination == "/app/chat.sendPrivateMessage":
                payload = ChatMessageCreate(
                    sender=body.get("sender"),
                    receiver=body.get("receiver"),
                    content=body.get("content", ""),
                    messageType=body.get("messageType", "PRIVATE_MESSAGE"),
                    timeStamp=body.get("timeStamp"),
                )
                if payload.sender and payload.receiver and user_exists(db, payload.sender) and user_exists(db, payload.receiver):
                    message = save_chat_message(db, payload)
                    await manager.send_to_user(payload.receiver, serialize_message(message))
                    await manager.send_to_user(payload.sender, serialize_message(message))

    except WebSocketDisconnect:
        username = manager.disconnect(websocket)
        if username:
            set_user_online_status(db, username, False)
            payload = ChatMessageCreate(
                sender=username,
                content="",
                messageType="LEAVE",
                timeStamp=datetime.utcnow(),
            )
            message = save_chat_message(db, payload)
            await manager.broadcast(serialize_message(message))
    except Exception:
        manager.disconnect(websocket)
