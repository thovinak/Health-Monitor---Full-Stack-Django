from django.urls import path

from . import views

app_name = 'tabulation'
urlpatterns = [
    path('', views.index, name='index'),
    path("sinewave/", views.sine_wave, name='sine_wave'),
    path("ecgsignal/", views.heart_beat, name='heartbeat'),
]
