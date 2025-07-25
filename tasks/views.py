from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Work with database
# Transform data
# Data pass
# http response/ json response

def home(request):
    return HttpResponse("Welcome to task management")

def contact(request):
    return HttpResponse("<h1 style='color: red'>Contact us at 3494626331</h1>")

def show_task(request):
    return HttpResponse("This is Show task")