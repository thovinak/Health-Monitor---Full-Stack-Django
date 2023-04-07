#  Copyright (c) 2023 - All rights reserved.
#  Created by [Karthik Thovinakere] for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I [Karthik Thovinakere], [400140562] certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from . import forms


@login_required(login_url='/accounts/login/')
def index(request):
    page = 'accounts/index.html'
    if request.user.is_authenticated:
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = "profile_pictures/user_placeholder.svg"

    context = {
        "profile_picture": profile_picture
    }
    return render(request, template_name=page, context=context)


def signup(request):
    page = 'accounts/signup.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/')
    else:
        form = UserCreationForm()

    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = "profile_pictures/user_placeholder.svg"

    context = {
        "form": form,
        "profile_picture": profile_picture
    }
    return render(request, page, context)


@login_required(login_url='/accounts/login/')
def edit_settings(request):
    if request.method == 'POST':
        user_form = forms.UpdateUserForm(request.POST, instance=request.user)
        profile_form = forms.UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Your profile is updated successfully')
            return redirect(to='index')
    else:
        user_form = forms.UpdateUserForm(instance=request.user)
        profile_form = forms.UpdateProfileForm(instance=request.user.profile)
        if request.user.is_authenticated:
            profile_picture = request.user.profile.profile_picture
        else:
            profile_picture = "profile_pictures/"
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'profile_picture': profile_picture
        }

    return render(request, 'accounts/settings.html', context)
