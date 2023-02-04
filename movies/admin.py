from django.contrib import admin
from . models import *

# Register your models here.


class MoviesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('movie_title',)}
    list_display = ('movie_title', 'id')


admin.site.register(Movies, MoviesAdmin)