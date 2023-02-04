from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from rest_framework import generics
from .serializers import ShowSerializer, SeatSerializer
from .models import MovieShow, Seats
from theaters.models import Theaters
from theaters.serializers import TheaterSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

class MovieShowList(CreateView):
    template_name = 'shows/movieshowlist.html'
    model = MovieShow
    fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shows = MovieShow.objects.filter(movie__id=self.kwargs['id'])
        context = {
            'shows': shows
        }
        print(context)
        return context


class SeatLayout(TemplateView):
    template_name = 'shows/seatlayout.html'
    

# api views


@api_view(['GET', 'POST'])
def listshow(request, pk):
    data = request.data
    date = data['date']
    shows = MovieShow.objects.filter(movie__id=pk, date=date)
    print(date)
    serializer = ShowSerializer(shows, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def allshows(request):
    shows = MovieShow.objects.all()
    serializer = ShowSerializer(shows, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def showbyid(request, pk):
    shows = MovieShow.objects.get(id=pk)
    serializer = ShowSerializer(shows, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def listtheatrshow(request):
    shows = MovieShow.objects.filter(movie__id=1, theater__id=1)
    print(shows)
    serializer = ShowSerializer(shows, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def seatlist(request, pk):
    seat = Seats.objects.filter(show__id=pk)
    serializer = SeatSerializer(seat, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def show_by_t(request):
    theater = Theaters.objects.get(id=1)
    show = MovieShow.objects.filter(theater=theater)
    serializer = ShowSerializer(show, many=True)
    return Response(serializer.data)