from django.contrib import admin

from theaters.models import Seat, Screen, Row

admin.site.register(Seat)
admin.site.register(Row)
admin.site.register(Screen)
