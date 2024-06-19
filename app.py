from flask import Flask
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Socket IO
socketio = SocketIO(app,cors_allowed_origins='*')

@socketio.on('connect')
def connect():
    print("Client connected")

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('battery')
def setBatLevel(data):
    print(data)
    if(data['percent'] >= 60):
        os.system("notify-send 'Phone charge at {}'".format(data['percent']))

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

@app.get("/")
def root():
    return {"msg":"Hello world"}

print("server is up")

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0")
