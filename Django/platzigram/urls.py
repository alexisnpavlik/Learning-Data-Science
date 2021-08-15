"""platzigram URL module"""
from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world',views.hello_world),
]

urlpatterns = [
    path('hi',views.hi),
]