from django.db import models


class SineData(models.Model):
    data_val = models.DecimalField(decimal_places=20, max_digits=30)
    label = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['-label']


class HeartBeatData(models.Model):
    value = models.DecimalField(decimal_places=25, max_digits=30)
    time_stamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time_stamp']
