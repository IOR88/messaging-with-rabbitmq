from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.TextField(unique=True)
    members = models.ManyToManyField('auth.User')


class Message(models.Model):
    datetime = models.DateTimeField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
