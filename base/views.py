from django.shortcuts import render

# Create your views here.

rooms = [
  {'id': 1, 'name': 'Lets Learn Python!'},
  {'id': 2, 'name': 'Design with Me'},
  {'id': 3, 'name': 'Frontend Developers'},
]

def home(req):
  context = {'rooms': rooms}
  return render(req, 'base/home.html', context)

def room(req, pk):
  return render(req, 'base/room.html')