from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    """Returns a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f"la hora ahora es {now}")

def hi(request):
    return HttpResponse("hi")