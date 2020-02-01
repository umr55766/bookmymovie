from django.db import models
from django_extensions.db.models import TimeStampedModel


class Screen(TimeStampedModel):
    name = models.CharField(max_length=1024)


class Row(TimeStampedModel):
    serial = models.CharField(max_length=2)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)


class Seat(TimeStampedModel):
    number = models.IntegerField()
    is_aisle = models.BooleanField(default=False)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
