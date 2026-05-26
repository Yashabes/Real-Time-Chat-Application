from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import or_, asc, desc

from models.chat_message import ChatMessage
from schemas.message import ChatMessageCreate


def save_chat_message(db: Session, payload: ChatMessageCreate) -> ChatMessage:
    message = ChatMessage(
        content=payload.content or "",
        sender=payload.sender,
        receiver=payload.receiver,
        color=payload.color,
        time_stamp=payload.timeStamp or datetime.utcnow(),
        message_type=payload.messageType,
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_public_messages(db: Session) -> List[ChatMessage]:
    return (
        db.query(ChatMessage)
        .filter(ChatMessage.message_type == "CHAT")
        .order_by(asc(ChatMessage.time_stamp))
        .all()
    )


def get_recent_messages(db: Session, limit: int = 50) -> List[ChatMessage]:
    return (
        db.query(ChatMessage)
        .filter(ChatMessage.message_type == "CHAT")
        .order_by(desc(ChatMessage.time_stamp))
        .limit(limit)
        .all()
    )


def get_private_messages(db: Session, user1: str, user2: str) -> List[ChatMessage]:
    return (
        db.query(ChatMessage)
        .filter(
            ChatMessage.message_type == "PRIVATE_MESSAGE",
            or_(
                (ChatMessage.sender == user1) & (ChatMessage.receiver == user2),
                (ChatMessage.sender == user2) & (ChatMessage.receiver == user1),
            ),
        )
        .order_by(asc(ChatMessage.time_stamp))
        .all()
    )
