from django.shortcuts import render

# Create your views here.

rooms = [
  {'id': 1, 'name': 'Lets Learn Python!'},
  {'id': 2, 'name': 'Design with Me'},
  {'id': 3, 'name': 'Frontend Developers'},
]

def home(req):
  return render(req, 'home.html', {'rooms': rooms})

def room(req):
  return render(req, 'room.html')