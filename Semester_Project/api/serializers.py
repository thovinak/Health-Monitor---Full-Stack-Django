from rest_framework import serializers

from . import models


class SineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SineData
        fields = ['url', 'data_val', 'label']
