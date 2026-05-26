from fastapi import FastAPI

from app.routes import auth
from app.routes import messages
from app.routes import websocket

app=FastAPI()

app.include_router(auth.router)

app.include_router(messages.router)

app.include_router(websocket.router)

@app.get("/")

def root():

 return {
  "status":"running"
 }