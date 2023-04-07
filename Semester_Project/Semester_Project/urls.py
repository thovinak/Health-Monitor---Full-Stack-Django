"""Semester_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#  Copyright (c) 2023 - All rights reserved.
#  Created by [Karthik Thovinakere] for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I [Karthik Thovinakere], [400140562] certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path("admin/", admin.site.urls),
                  path("dashboard/", include('dashboard.urls', namespace='dashboard')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path("tabulation/", include('tabulation.urls', namespace='tabulation')),
                  path("accounts/", include('accounts.urls')),
                  path("api/", include('api.urls')),
                  path("fourier/", include('fourier.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
