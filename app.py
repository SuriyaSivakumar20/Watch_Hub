import os
from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, join_room, leave_room, emit
from werkzeug.utils import secure_filename

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

rooms = {}  # Store rooms and users

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return "No file part", 400
    file = request.files['video']
    if file.filename == '':
        return "No selected file", 400
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    return file_path  # Return file path for frontend usage

@socketio.on('create-room')
def create_room(data):
    roomId = data['roomId']
    if roomId not in rooms:
        rooms[roomId] = {'users': [], 'owner': request.sid}
    join_room(roomId)
    rooms[roomId]['users'].append(request.sid)
    emit('room-update', rooms[roomId]['users'], room=roomId)

@socketio.on('join-room')
def join_existing_room(data):
    roomId = data['roomId']
    if roomId in rooms:
        join_room(roomId)
        rooms[roomId]['users'].append(request.sid)
        emit('room-update', rooms[roomId]['users'], room=roomId)

@socketio.on('sync-video')
def sync_video(data):
    emit('sync-video', data, room=data['roomId'], include_self=False)

@socketio.on('moderator-control')
def moderator_control(data):
    if request.sid == rooms[data['roomId']]['owner']:  # Only room owner can control playback
        emit('moderator-control', data, room=data['roomId'], include_self=False)

@socketio.on('disconnect')
def on_disconnect():
    for roomId in list(rooms.keys()):
        if request.sid in rooms[roomId]['users']:
            rooms[roomId]['users'].remove(request.sid)
            emit('room-update', rooms[roomId]['users'], room=roomId)

if __name__ == '__main__':
    socketio.run(app, debug=True)
