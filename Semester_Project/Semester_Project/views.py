from django.shortcuts import render
from django.contrib import auth


def index(request):
    data = ""
    user_details = auth.get_user(request)
    profile_picture = '/static/images/user_placeholder.svg'
    context = {
        'data': data,
        'profile_picture': profile_picture
    }
    return render(request, 'index.html', context)
