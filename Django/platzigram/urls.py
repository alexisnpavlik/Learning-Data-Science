"""platzigram URL module"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    """Returns a greeting"""
    return HttpResponse("hello word!")

urlpatterns = [
    path('hello-word',hello_world),
]
