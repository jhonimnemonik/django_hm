from django.shortcuts import redirect
from django.urls import path
from loader import views as loader

urlpatterns = [path('', loader.photo_load, name='photo_load')]
