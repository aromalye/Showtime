from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
# from rest_framework import generics
# from .serializers import ShowSerializers, SeatSearializers
from .models import MovieShow


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
    



# class ShowListView(generics.ListAPIView):
#     serializer_class = ShowSerializers

#     def get_queryset(self):
#         movie_id = self.kwargs['movie_id']
#         return Shows1.objects.filter(movie=movie_id)


# class ShowdetailsView(generics.RetrieveAPIView):
#     queryset = Shows1.objects.all()
#     serializer_class = ShowSerializers


# class SeatListView(generics.ListAPIView):
#     serializer_class = SeatSearializers
#     queryset = ShowSeats.objects.all()