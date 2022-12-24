from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1><marquee>just go to hell and heaven</marquee></h1>')

def second(request):
    return HttpResponse('<h1><marquee>your project may not work properly until u r right</marquee></h1>')

# Create your views here.
