from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse("Welcome to the meeting Planner!")

def date(request):
    return HttpResponse("This page was served at" + str(datetime.now()))

def about_me(request):
    return HttpResponse("I'm 24, yo")