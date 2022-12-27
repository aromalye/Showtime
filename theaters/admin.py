from django.contrib import admin
from . models import *
# Register your models here


class TheaterAdmin(admin.ModelAdmin):
    list_display = ('theater_name','district')


admin.site.register(Theaters, TheaterAdmin)
