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
