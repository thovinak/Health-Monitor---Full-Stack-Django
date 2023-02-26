from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path("sinewave", views.sinewave, name='sinewave'),
]
