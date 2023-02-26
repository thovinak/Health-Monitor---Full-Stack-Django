from django.db import models


# Create your models here.
class SineData(models.Model):
    value = models.DecimalField(decimal_places=32, max_digits=32)
    label = models.TimeField(auto_now=True)
