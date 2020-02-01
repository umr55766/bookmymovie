from django.db import models
from django_extensions.db.models import TimeStampedModel

from theaters.models import Seat


class Reservation(TimeStampedModel):
    reserved_seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
