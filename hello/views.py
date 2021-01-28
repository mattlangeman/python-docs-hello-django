from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, World! Welcome to the web. Tagged release-0.1.1")
