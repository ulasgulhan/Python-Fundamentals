from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Room


# Create your views here.


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})


def detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, 'rooms/detail.html', {'room': room})

