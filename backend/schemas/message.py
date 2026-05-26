from __future__ import annotations
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ChatMessageBase(BaseModel):
    content: Optional[str] = Field(default="")
    sender: Optional[str] = None
    receiver: Optional[str] = None
    color: Optional[str] = None
    timeStamp: Optional[datetime] = Field(default=None, alias="timeStamp")
    messageType: Optional[str] = Field(default=None, alias="messageType")


class ChatMessageCreate(ChatMessageBase):
    messageType: str


class ChatMessageResponse(BaseModel):
    id: int
    content: Optional[str] = None
    sender: Optional[str] = None
    receiver: Optional[str] = None
    color: Optional[str] = None
    timeStamp: datetime = Field(alias="timeStamp")
    messageType: str = Field(alias="messageType")

    model_config = {
        "from_attributes": True,
        "populate_by_name": True,
    }
