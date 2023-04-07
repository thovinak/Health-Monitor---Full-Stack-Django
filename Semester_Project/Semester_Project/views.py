#  Copyright (c) 2023 - All rights reserved.
#  Created by [Karthik Thovinakere] for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I [Karthik Thovinakere], [400140562] certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.shortcuts import render
from django.contrib import auth


# def index(request):
#     if request.user.is_authenticated:
#         profile_picture = request.user.profile.profile_picture
#     else:
#         profile_picture = '/static/images/user_placeholder.svg'
#
#     context = {
#         'profile_picture': profile_picture
#     }
#     return render(request, 'index.html', context)


def index(request):
    if request.user.is_authenticated:
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = "profile_pictures/user_placeholder.svg"
    context = {
        'profile_picture': profile_picture
    }
    return render(request, 'index.html', context)
