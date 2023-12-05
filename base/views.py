from django.shortcuts import render

# Create your views here.
def home(req):
  return render(req, 'home.html')

def room(req):
  return render(req, 'room.html')