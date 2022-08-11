from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Restaurant, Menu, Reservation
from .forms import ReservationForm

class RestaurantList(generic.ListView):
    model = Restaurant
    template_name = 'index.html'

class MenuList(generic.ListView):
    model = Menu
    template_name = 'menu.html'

class ReservationList(generic.ListView):
    model = Reservation
    template_name = 'reservation.html'