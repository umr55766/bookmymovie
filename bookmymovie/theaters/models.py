from django.db import models
from django_extensions.db.models import TimeStampedModel


class Seat(TimeStampedModel):
    row = models.CharField(max_length=2)
    number = models.IntegerField()
    is_aisle = models.BooleanField(default=False)


class Theater(TimeStampedModel):
    name = models.CharField(max_length=1024)
    seats = models.ForeignKey(Seat, on_delete=models.CASCADE)
