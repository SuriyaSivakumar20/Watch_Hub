from fastapi import FastAPI
import socketio
import random
import string

app = FastAPI()
sio = socketio.AsyncServer(cors_allowed_origins="*")
socket_app = socketio.ASGIApp(sio, app)

# Store active rooms
rooms = {}

def generate_room_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.get("/")
async def home():
    return {"message": "Watch Party Hub Backend Running"}

@app.get("/create-room")
async def create_room():
    room_id = generate_room_id()
    rooms[room_id] = []
    return {"room_id": room_id}

@sio.on("join")
async def join_room(sid, data):
    room = data["room"]
    sio.enter_room(sid, room)
    if room not in rooms:
        rooms[room] = []
    rooms[room].append(sid)
    await sio.emit("user_joined", {"message": f"User {sid} joined"}, room=room)

@sio.on("sync_video")
async def sync_video(sid, data):
    room = data["room"]
    await sio.emit("update_video", data, room=room, skip_sid=sid)

@sio.on("chat_message")
async def chat_message(sid, data):
    room = data["room"]
    await sio.emit("receive_message", data, room=room, skip_sid=sid)

@app.get("/end-room/{room_id}")
async def end_room(room_id: str):
    if room_id in rooms:
        del rooms[room_id]
    return {"message": "Room ended"}

app.mount("/", socket_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
