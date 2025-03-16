import socketio

sio = socketio.AsyncServer(async_mode="asgi")
sio_app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print(f"Socket.IO client connected: {sid}")
    await sio.emit("message", {"message": "Socket.IO ulanish muvaffaqiyatli!"}, to=sid)

@sio.event
async def disconnect(sid):
    print(f"Socket.IO client disconnected: {sid}")
