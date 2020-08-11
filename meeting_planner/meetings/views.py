from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from meetings.models import Meeting, Room


def detail(request, id):
    #    meeting = Meeting.objects.get(pk=id) pk->primary key-> the row with this unique id
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms(request):
    return render(request, "meetings/rooms.html",
                  {"rooms": Room.objects.all()})

def new(request):
    return render(request, "meetings/new.html")