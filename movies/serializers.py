from rest_framework import serializers
from . models import *

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
        