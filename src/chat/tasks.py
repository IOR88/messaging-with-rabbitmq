import socketio
from mwr import celery_app as app
import logging
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
CELERY_APP_NAME = app.main

url = 'amqp://guest:guest@localhost:5672//'
sio = socketio.KombuManager(url)


@app.task(bind=True, name='{app}-{task}'.format(app=CELERY_APP_NAME, task='testing1'))
def testing(self, message):
    # testing receiving message and passing it to socketio exchange in RabbitMQ which pass it to
    # bind queues, socket.io server consume message with client manager and notify all users.
    sio.emit('testing', {'data': message})
    logger.info('Testing message: ', message)
