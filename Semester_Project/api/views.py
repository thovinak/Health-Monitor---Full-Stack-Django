#  Copyright (c) 2023 - All rights reserved.
#  Created by [Karthik Thovinakere] for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I [Karthik Thovinakere], [400140562] certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from rest_framework import permissions, viewsets

from . import models
from .serializers import SineSerializer


# Create your views here.

class SineDataView(viewsets.ModelViewSet):
    '''
        API Endpoint that allows the SineData to be viewed
    '''
    queryset = models.SineData.objects.all().order_by('-label')[:1000]
    serializer_class = SineSerializer
    permission_classes = [permissions.AllowAny]
