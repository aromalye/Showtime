from rest_framework import serializers
from . models import *
from movies.serializers import MovieSerializers
from theaters.serializers import TheaterSerializers


class ShowSerializer(serializers.ModelSerializer):
    movie=MovieSerializers(many=False)
    theater=TheaterSerializers(many=False)
    class Meta:
        model = MovieShow
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    show = ShowSerializer(many=False)
    class Meta:
        model = Seats
        fields = '__all__'



