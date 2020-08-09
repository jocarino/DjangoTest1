from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This data was sent from view to the template"})

def date(request):
    return HttpResponse("This page was served at" + str(datetime.now()))

def about_me(request):
    return HttpResponse("I'm 24, yo")