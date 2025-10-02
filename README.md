# Realtime Chat App - One Port Setup
# Realtime Chat App - One Port Setup
# Realtime Chat App - One Port (Frontend 5173)

This setup runs the backend on 8081 and the frontend behind Nginx, exposed on http://localhost:5173. The frontend proxies API/WebSocket traffic to the backend at 8081.

## Prerequisites
- Docker and Docker Compose installed
- MySQL running on your host at 3306 with database `RealTimeChatApp` and the configured credentials

## Run
This project is configured to run the backend (Spring Boot, port 8081) and frontend (React + Vite) together behind a single port using Docker.

What you get:
- Frontend served at http://localhost:8080
- API and WebSocket requests are transparently proxied to the backend at 8081
- No CORS hassles, single origin

## Prerequisites
- Docker and Docker Compose installed

## Run
This project is configured to run the backend (Spring Boot) and frontend (React + Vite) together behind a single port using Docker.

What you get:
- Frontend served at http://localhost:8080
- API and WebSocket requests are transparently proxied to the backend
- No CORS hassles, single origin

## Prerequisites
- Docker and Docker Compose installed

## Run
