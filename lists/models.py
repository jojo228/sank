from django.db import models
from main import models as main_models


class List(main_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"
