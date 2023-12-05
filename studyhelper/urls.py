from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(req):
  return HttpResponse('Home Page')

def room(req):
  return HttpResponse('Room')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room)
]
