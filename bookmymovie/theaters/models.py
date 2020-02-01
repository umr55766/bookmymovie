from django.db import models
from django_extensions.db.models import TimeStampedModel


class Theater(TimeStampedModel):
    name = models.CharField(max_length=1024)


class Seat(TimeStampedModel):
    row = models.CharField(max_length=2)
    number = models.IntegerField()
    is_aisle = models.BooleanField(default=False)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
