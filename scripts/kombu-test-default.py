# https://github.com/celery/kombu#quick-overview

from kombu import Connection, Exchange, Queue

media_exchange = Exchange('media', 'direct', durable=True)
video_queue = Queue('video', exchange=media_exchange, routing_key='video')


def process_media(body, message):
    print(body, 'WOW :)')
    message.ack()


# connections
with Connection('amqp://guest:guest@localhost:5672//') as conn:
    # produce
    producer = conn.Producer(serializer='json')
    producer.publish({'name': '/tmp/lolcat1.avi', 'size': 1301013},
                     exchange=media_exchange, routing_key='video',
                     declare=[video_queue])

    # the declare above, makes sure the video queue is declared
    # so that the messages can be delivered.
    # It's a best practice in Kombu to have both publishers and
    # consumers declare the queue. You can also declare the
    # queue manually using:
    #     video_queue(conn).declare()

    # consume
    with conn.Consumer(video_queue, callbacks=[process_media]) as consumer:
        # Process messages and handle events on all channels
        while True:
            conn.drain_events()
