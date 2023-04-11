from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    return HttpResponse('This is the Home Page')

def roomView(request):
    return HttpResponse('This is the default Room Page')