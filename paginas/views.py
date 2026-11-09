# paginas/views.py
from django.http import HttpResponse


def vista_inicio(request):
    return HttpResponse("Hello, World!")
