from django.urls import path

from . import views

app_name = 'tabulation'
urlpatterns = [
    path('', views.index, name='index'),
    path("sinewave/", views.sine_wave, name='sine_wave'),
]
