#  Copyright (c) 2023.

from django.urls import path

from . import views

app_name = 'fourier'
urlpatterns = [
    path('', views.index, name='index'),
    path("sinewave/", views.sin_wave, name='sin_wave'),
    # path("heartbeat/", views.heart_beat, name='heartbeat'),
]
