from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic, models
from .form import RoomForm


# must the same quotation marks between key-name and value
# rooms = [ 
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Backend Developer'}
# ]


# Perform home page
def home(request):
    rooms = Room.objects.all()

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=str(pk))
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save() # save to the database
            return redirect(home)

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)  # passing the above room

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect(home)

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj': room}
    return render(request, 'base/delete.html', context)