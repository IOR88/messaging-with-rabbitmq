from django.core.management.base import BaseCommand, CommandError
from chat import models


class Command(BaseCommand):
    help = 'Adding dump data for chat application'

    def handle(self, *args, **options):
        # add one default room
        room = models.Room(name='Main')
        room.save()
