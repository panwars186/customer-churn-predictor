from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world from Django and Jenknins")

# Create your views here.
