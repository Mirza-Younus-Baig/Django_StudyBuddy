from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name = 'HomeView'),
    path('room', views.roomView, name = 'RoomView'),

]