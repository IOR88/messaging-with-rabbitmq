import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web

import socketio

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

url = 'amqp://guest:guest@localhost:15672//'
sio = socketio.AsyncServer(async_mode='tornado', cors_allowed_origins='http://localhost:8000',
                           client_manager=socketio.KombuManager(url))


@sio.event
async def connect(sid, environ):
    # broadcast
    await sio.emit('connect', {'data': ':)'})


@sio.event
async def disconnect(sid):
    # broadcast
    await sio.emit('disconnect', {'data': ':('})


def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/socket.io/", socketio.get_tornado_handler(sio)),
        ],
        debug=options.debug,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()