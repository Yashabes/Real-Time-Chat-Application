from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from database import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(2000), nullable=True)
    sender = Column(String(255), nullable=True)
    receiver = Column(String(255), nullable=True)
    color = Column(String(50), nullable=True)
    time_stamp = Column(DateTime, nullable=False, server_default=func.now())
    message_type = Column(String(50), nullable=False)
