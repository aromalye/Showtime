from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesList.as_view(), name='movie'),
    path('details/<str:id>/', views.MoviesDetails.as_view(), name='moviedetail'),


    path('api/', views.MoviesListView.as_view(), name='movieslist'),
    path('api/<pk>/', views.MovieDetailView.as_view(), name='moviedetails'),
]