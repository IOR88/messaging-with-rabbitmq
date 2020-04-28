from mwr import celery_app as app
from django.contrib import auth
import logging
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
CELERY_APP_NAME = app.main


@app.task(bind=True, name='{app}-{task}'.format(app=CELERY_APP_NAME, task='testing'))
def testing(self, message):
    # total_users = auth.models.User.objects.filter(is_active=True).count()
    app.send_task('mwr-chat-testing', kwargs={"message": message})
    logger.info('Testing message: ', message)
