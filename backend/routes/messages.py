from fastapi import APIRouter

router=APIRouter(
 prefix="/api/messages"
)

@router.get("/public")
def public_messages():

    return []

@router.get("/private")
def private_messages():

    return []