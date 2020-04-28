from chat_server import celery_app as app
from celery.utils.log import get_task_logger
import socketio
logger = get_task_logger(__name__)
# pyamqp://guest@localhost//
# sio = socketio.KombuManager()

CELERY_APP_NAME = app.main


@app.task(bind=True, name='{app}-{task}'.format(app=CELERY_APP_NAME, task='testing'))
def testing(self, message):
    # sio.emit('testing', {'data': message})
    logger.info('Testing message emitted - {0}'.format(message))
