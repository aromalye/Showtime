from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('showlist/<int:id>', MovieShowList.as_view(), name='movieshowlist'),
    path('seatlayout/<int:id>', SeatLayout.as_view(), name='seatlayout'),

    path('allshows/', views.allshows, name='allshows'),
    path('listshow/<int:pk>/', views.listshow, name='listshow'),
    path('showbyid/<int:pk>/', views.showbyid, name='showbyid'),
    path('seatlist/<int:pk>/', views.seatlist, name='seatlist'),
    path('listtheatrshow/', views.listtheatrshow, name='listtheatrshow'),
    path('show_by_t/', views.show_by_t, name='show_by_t'),


#     path('api/<movie_id>', views.ShowListView.as_view(), name='showslist'),
#     path('api/<pk>/', views.ShowdetailsView.as_view(), name='showdetails'),
#     path('seat/', views.SeatListView.as_view(), name='seatlist'),
]