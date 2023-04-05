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
