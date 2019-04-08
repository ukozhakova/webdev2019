from django.shortcuts import render
from django.http import HttpResponse


def lyrics(request):
    return HttpResponse('<p>ddu du ddu du</p>')


def welcome(request):
    return HttpResponse('<h1>Welcome to my site</h1>')