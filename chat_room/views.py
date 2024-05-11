from django.shortcuts import render
from chat_room.models import Room

def index(request):
    return render(request, 'index.html', {'rooms': Room.objects.all()})


def room(request, room_name):
    #created becomes False if the existing room is found and True if not found and new room is created
    #chat_room holds the object as roomn_name in case of presence
    chat_room, created = Room.objects.get_or_create(name=room_name)

    return render(request, 'room.html', {'room': chat_room})


