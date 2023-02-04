from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.TheatersListView.as_view(), name='theaterslist'),
    path('api/<pk>/', views.TheaterdetailsView.as_view(), name='theaterdetails'),

    path('listtheater/', views.listtheater, name='listtheater'),
]