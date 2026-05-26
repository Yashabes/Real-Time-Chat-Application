from typing import Dict, Optional
from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.websocket_to_username: Dict[int, str] = {}

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.websocket_to_username[id(websocket)] = ""

    def register_user(self, username: str, websocket: WebSocket) -> None:
        self.active_connections[username] = websocket
        self.websocket_to_username[id(websocket)] = username

    def disconnect(self, websocket: WebSocket) -> Optional[str]:
        socket_id = id(websocket)
        username = self.websocket_to_username.pop(socket_id, None)
        if username and username in self.active_connections:
            self.active_connections.pop(username, None)
        return username

    async def broadcast(self, message: dict) -> None:
        for connection in list(self.active_connections.values()):
            try:
                await connection.send_json(message)
            except Exception:
                pass

    async def send_to_user(self, username: str, message: dict) -> None:
        connection = self.active_connections.get(username)
        if connection:
            try:
                await connection.send_json(message)
            except Exception:
                pass

    def get_username(self, websocket: WebSocket) -> Optional[str]:
        return self.websocket_to_username.get(id(websocket))


manager = ConnectionManager()
