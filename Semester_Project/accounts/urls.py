#  Copyright (c) 2023 - All rights reserved.
#  Created by [Karthik Thovinakere] for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I [Karthik Thovinakere], [400140562] certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [

    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('settings/', views.edit_settings, name='settings')
]
