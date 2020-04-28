# https://github.com/celery/kombu#quick-overview

from kombu import Connection, Exchange, Queue

options = {'type': 'fanout', 'durable': False}
channel = 'socketio'
socket_io_exchange = Exchange(channel, **options)
socket_io_queue = Queue('kombu-test-socket-io', exchange=socket_io_exchange, routing_key='socketio')


def process_message(body, message):
    print(body, 'WOW :)')
    message.ack()


# connections
with Connection('amqp://guest:guest@localhost:5672//') as conn:
    # we want to consume on socketio.KombuManager emit to check if messages can be consumed
    with conn.Consumer(socket_io_queue, callbacks=[process_message]) as consumer:
        # Process messages and handle events on all channels
        while True:
            conn.drain_events()
