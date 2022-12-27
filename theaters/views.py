from django.shortcuts import render
from rest_framework import generics
from . models import Theaters
from . serializers import TheaterSerializers


# Create your views here.


class TheatersListView(generics.ListAPIView):
    location = "TVM"
    queryset = Theaters.objects.filter(district=location)
    serializer_class = TheaterSerializers


class TheaterdetailsView(generics.RetrieveAPIView):
    queryset = Theaters.objects.all()
    serializer_class = TheaterSerializers