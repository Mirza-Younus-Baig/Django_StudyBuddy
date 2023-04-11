from django.shortcuts import render


# Create your views here.
def homeView(request):
    return render(request, "home.html")

def roomView(request):
    return render(request, "room.html")