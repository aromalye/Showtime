from django.contrib import admin
from .models import MovieShow
# Register your models here.

class MovieShowAdmin(admin.ModelAdmin):
    list_display = ['movie', 'theater', 'time', 'date']

admin.site.register(MovieShow, MovieShowAdmin)