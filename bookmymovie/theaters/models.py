from django.db import models


class Seat(models.Model):
    row = models.CharField(max_length=2)
    number = models.IntegerField()
    is_aisle = models.BooleanField(default=False)


class Theater(models.Model):
    name = models.CharField(max_length=1024)
    seats = models.ForeignKey(Seat, on_delete=models.CASCADE)
