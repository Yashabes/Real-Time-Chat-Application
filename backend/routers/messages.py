from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas.message import ChatMessageResponse
from services.message_service import get_public_messages, get_private_messages, get_recent_messages

router = APIRouter(prefix="/api/messages", tags=["messages"])


@router.get("/private", response_model=List[ChatMessageResponse])
def get_private_messages_route(
    user1: str = Query(...),
    user2: str = Query(...),
    db: Session = Depends(get_db),
):
    return get_private_messages(db, user1, user2)


@router.get("/public", response_model=List[ChatMessageResponse])
def get_public_messages_route(db: Session = Depends(get_db)):
    return get_public_messages(db)


@router.get("/recent", response_model=List[ChatMessageResponse])
def get_recent_messages_route(
    limit: int = Query(50, ge=1),
    db: Session = Depends(get_db),
):
    return get_recent_messages(db, limit)
