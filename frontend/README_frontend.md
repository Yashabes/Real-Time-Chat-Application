Realtime Chat App - Frontend (Vite + React)

This is a minimal React frontend for the provided Spring Boot realtime chat backend.

Features
- Register and Login pages
- HTTP-only JWT cookie support (via withCredentials)
- Public room via STOMP over SockJS (/topic/public)
- Private messages via per-user queue (/user{username}/queue/private)
- Simple, clean UI with message list and inputs

Backend assumptions
- Backend runs at http://localhost:8081 (default). You can change this using VITE_BACKEND_URL.
- STOMP endpoint: /ws with SockJS
- Application destination prefix: /app
- Public topic: /topic/public
- Private queue destination: /user{username}/queue/private
- REST endpoints:
  - POST /api/auth/register-user { username, email, password }
  - POST /api/auth/login { username, password } -> Sets HTTP-only cookie and returns user object
  - POST /api/auth/logout
  - GET  /api/auth/getcurrentuser -> returns current user

Important: Local dev and secure cookies
The backend sets the JWT cookie with the Secure flag. Browsers only store/send Secure cookies over HTTPS. If you run the frontend and backend on plain HTTP locally, the cookie may not be stored, and authenticated routes may fail.

Workarounds during development:
1) Use HTTPS for local frontend dev server. One quick option is to run Vite with HTTPS using a local certificate (mkcert or self-signed). Then set VITE_BACKEND_URL to https://localhost:8081 and run the backend with HTTPS too; or
2) Temporarily adjust the backend cookie to not use secure(true) for local development only; or
3) Use a reverse proxy (e.g., Nginx, Caddy, Traefik) with TLS terminating in front of both services.

Getting started
1) Install dependencies
   cd frontend
   npm install

2) Configure environment (optional)
   # create an .env file if needed
   echo VITE_BACKEND_URL=http://localhost:8081 > .env

3) Run dev server
   npm run dev

4) Open the app
   http://localhost:5173

Notes
- The Vite dev proxy is configured for /api and /ws to the backend; however, SockJS is initialized directly with VITE_BACKEND_URL to avoid tricky path edge-cases. You can switch to relative paths if you prefer using the proxy entirely.
- The backend’s MessageController currently lacks an explicit mapping (e.g., @GetMapping). The frontend doesn’t fetch historical messages and only displays messages from the current session.
- Private message queue path is intentionally /user{username}/queue/private to match the backend’s convertAndSend destination.

File map (key parts)
- /frontend
  - index.html
  - vite.config.js
  - src/
    - api/axios.js (axios instance with withCredentials)
    - context/AuthContext.jsx (auth state + actions)
    - App.jsx (routes + protected route)
    - pages/Login.jsx
    - pages/Register.jsx
    - pages/Chat.jsx (STOMP/SockJS; public + private)
    - components/MessageList.jsx, MessageInput.jsx

