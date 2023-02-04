from django.shortcuts import render
from rest_framework import generics
from . models import Theaters
from . serializers import TheaterSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.


class TheatersListView(generics.ListAPIView):
    location = "TVM"
    queryset = Theaters.objects.filter(district=location)
    serializer_class = TheaterSerializers


class TheaterdetailsView(generics.RetrieveAPIView):
    queryset = Theaters.objects.all()
    serializer_class = TheaterSerializers


@api_view(['GET'])
def listtheater(request):
    shows = Theaters.objects.filter(showtime__id=1)
    print(shows)
    serializer = TheaterSerializers(shows, many=True)
    return Response(serializer.data)