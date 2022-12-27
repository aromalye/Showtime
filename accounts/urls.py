from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', views.userlogout, name='logout'),


    # api
    path('register_user/', views.register_user, name='register_user'),
]