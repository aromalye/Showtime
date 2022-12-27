from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView
from rest_framework import generics
from . models import *
from . serializers import *

# Create your views here.

class MoviesList(CreateView):
    template_name = 'movies/movie.html'
    model = Movies
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movies.objects.all()
        return context


class MoviesDetails(CreateView):
    template_name = 'movies/moviedetails.html'
    model = Movies
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = get_object_or_404(Movies, id=self.kwargs['id'])
        context = {
            'movie': movie
        }
        return context



# api views
class MoviesListView(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializers


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializers

