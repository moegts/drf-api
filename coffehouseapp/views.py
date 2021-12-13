from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import CoffeHouse
from .serializer import coffeSerializer

# Create your views here.


class coffeListView(generics.ListCreateAPIView):
    serializer_class = coffeSerializer
    queryset = CoffeHouse.objects.all()


class coffeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = coffeSerializer
    queryset = CoffeHouse.objects.all()