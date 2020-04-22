from rest_framework import serializers
from chat import models


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        exclude = ("members",)
