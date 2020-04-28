import socketio
from mwr import celery_app as app
from django.contrib import auth
import logging
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
CELERY_APP_NAME = app.main

# url = 'amqp://guest:guest@localhost:5672//'
sio = socketio.KombuManager()


@app.task(bind=True, name='{app}-{task}'.format(app=CELERY_APP_NAME, task='testing1'))
def testing(self, message):
    # testing receiving message and passing it to socket.io queue with socket.io client
    # app.send_task('mwr-testing2', kwargs={"message": message})
    sio.emit('testing', {'data': message})
    logger.info('Testing message: ', message)
