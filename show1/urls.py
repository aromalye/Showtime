from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('showlist/<int:id>', MovieShowList.as_view(), name='movieshowlist'),
    path('seatlayout/<int:id>', SeatLayout.as_view(), name='seatlayout'),


#     path('api/<movie_id>', views.ShowListView.as_view(), name='showslist'),
#     path('api/<pk>/', views.ShowdetailsView.as_view(), name='showdetails'),
#     path('seat/', views.SeatListView.as_view(), name='seatlist'),
]