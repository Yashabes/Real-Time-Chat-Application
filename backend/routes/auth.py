from fastapi import APIRouter

router=APIRouter(
    prefix="/api/auth"
)

@router.post("/register-user")
def register():

    return {
      "message":"registered"
    }

@router.post("/login")
def login():

    return {
       "token":"jwt"
    }