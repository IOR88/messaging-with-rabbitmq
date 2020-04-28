"""
Testing connection within the messaging stack Celery, RabbitMQ, PostgreSQL
"""
from celery import Celery

app = Celery('test', broker='pyamqp://guest:guest@localhost:5672//',
             backend='db+postgresql://postgres:1234abcd@localhost:5432/postgres')


@app.task
def add(x, y):
    return x + y


if __name__ == "__main__":
   add.delay(2, 2)
