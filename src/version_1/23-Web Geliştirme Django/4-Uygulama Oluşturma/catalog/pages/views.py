from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# http://127.0.0.1:8000

def index(request):
    return HttpResponse('<h1>Hello from pages app</h1>')
