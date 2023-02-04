from django.contrib import admin
from .models import MovieShow, Seats
# Register your models here.

class MovieShowAdmin(admin.ModelAdmin):
    list_display = ['movie', 'theater', 'time', 'date', 'id']


class SeatAdmin(admin.ModelAdmin):
    list_display = ['status', 'show', 'seatname', 'id']

admin.site.register(MovieShow, MovieShowAdmin)
admin.site.register(Seats, SeatAdmin)