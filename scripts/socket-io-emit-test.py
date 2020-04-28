import socketio

sio = socketio.KombuManager()
sio.emit('testing', {'data': 'TEST'})
