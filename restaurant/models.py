from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120, default='Kings Place')
    city = models.CharField(max_length=120, default='Kristiansund')
    country = models.CharField(max_length=120, default='Norway')

class Customer(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.email

class Table(models.Model):
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return str(self.seats)


class Reservation(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    party = models.ForeignKey('Customer', on_delete=models.CASCADE)
    spot = models.DateField()
    approved = models.BooleanField(default=False)

class Menu(models.Model):
    nameOfFood = models.CharField(max_length=30)
    meat = models.CharField(max_length=30)
    allergy = models.CharField(max_length=30)
    food_details = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=149)
