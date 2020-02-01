from django.http import JsonResponse

from api.v1.serializer import ScreenSeatSerializer
from theaters.models import Row


def seats_list_API(request):
    return JsonResponse(ScreenSeatSerializer({"seats": Row.objects.all()}).data)
