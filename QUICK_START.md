# Quick Start Guide - FastAPI Real-Time Chat Application

## Prerequisites

- Python 3.8+ (for backend)
- Node.js 16+ (for frontend)
- MySQL 5.7+ (already configured)

## Step 1: Start Backend (FastAPI Server)

```powershell
cd C:\Users\taliy\OneDrive\Desktop\rtca\backend
.\venv\Scripts\python.exe -m uvicorn main:app --host 0.0.0.0 --port 8081 --reload
```

Expected output:
```
INFO:     Will watch for changes in these directories: ['C:\Users\taliy\OneDrive\Desktop\rtca\backend']
INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxx] using WatchFiles
INFO:     Started server process [xxxx]
INFO:     Application startup complete
```

✅ Backend is ready when you see: `Application startup complete`

## Step 2: Start Frontend (React Dev Server)

```powershell
cd C:\Users\taliy\OneDrive\Desktop\rtca\frontend
npm run dev
```

Expected output:
```
  VITE v5.4.20  ready in xxxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

✅ Frontend is ready at: `http://localhost:5173`

## Step 3: Access the Application

Open your browser and go to:
```
http://localhost:5173
```

## Step 4: Test the Application

### Create User Account
1. Click "Register" (if you don't have an account)
2. Enter:
   - Username: `testuser`
   - Email: `test@example.com`
   - Password: `password123`
3. Click "Register"

### Login
1. Enter credentials
2. Click "Login"
3. You should see the chat interface

### Send Messages
1. **Public Chat**: Type in "Public Room" section and send
2. **Private Chat**: 
   - Click on a user from "Online Users" list
   - Type message and send

### Real-Time Features
- ✅ Messages appear instantly
- ✅ Online users list updates in real-time
- ✅ Connection status indicator shows 🟢 (connected) or 🔴 (disconnected)

---

## API Endpoints (Direct Access)

You can also test the API directly using `curl` or Postman:

### Register
```bash
curl -X POST http://localhost:8081/api/auth/register-user \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","email":"user1@test.com","password":"pass123"}'
```

### Login
```bash
curl -X POST http://localhost:8081/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"pass123"}'
```

### Get Online Users
```bash
curl http://localhost:8081/api/users/online
```

### Get Public Messages
```bash
curl http://localhost:8081/api/messages/public
```

---

## Troubleshooting

### Backend not starting?
1. Check Python is installed: `python --version`
2. Check venv is activated properly
3. Check MySQL connection: Database URL in `backend/.env` or `backend/config.py`

### Frontend not loading?
1. Check Node.js: `node --version`
2. Check npm packages: `npm install` in `frontend/` directory
3. Check port 5173 is not in use

### WebSocket not connecting?
1. Verify backend is running on port 8081
2. Check browser console for error messages
3. Ensure CORS is allowing `localhost:5173`

### Database errors?
1. Verify MySQL is running
2. Check database `RealTimeChatApp` exists
3. Verify credentials in `backend/.env`:
   ```
   DATABASE_URL=mysql+mysqlconnector://root:Virendra@123@localhost:3306/RealTimeChatApp
   ```

---

## File Locations

- **Backend code**: `C:\Users\taliy\OneDrive\Desktop\rtca\backend\`
- **Frontend code**: `C:\Users\taliy\OneDrive\Desktop\rtca\frontend\`
- **Database**: MySQL on `localhost` (default port 3306)

---

## Development Tips

### Hot Reload
- **Backend**: Automatically reloads when you edit Python files (uvicorn --reload)
- **Frontend**: Automatically reloads when you edit React components (Vite dev server)

### View API Documentation
- Swagger UI: `http://localhost:8081/docs`
- ReDoc: `http://localhost:8081/redoc`

### Check Database
```bash
# Using MySQL CLI
mysql -u root -p -h localhost
USE RealTimeChatApp;
SELECT * FROM users;
SELECT * FROM chat_messages;
```

---

## Production Deployment

When you're ready to deploy:

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8081
```

### Frontend
```bash
cd frontend
npm install
npm run build
# Serve the 'dist' folder with your web server (nginx, Apache, etc.)
```

---

## Support & Documentation

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Pydantic Docs**: https://docs.pydantic.dev/
- **SQLAlchemy Docs**: https://docs.sqlalchemy.org/
- **Vite Docs**: https://vitejs.dev/

---

**Status**: ✅ **FULL SPRING BOOT TO FASTAPI MIGRATION COMPLETE**

All backend functionality has been preserved. The frontend required only minimal WebSocket connection code changes.
