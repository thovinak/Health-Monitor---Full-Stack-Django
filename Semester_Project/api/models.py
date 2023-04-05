from django.db import models


# Create your models here.
class SineData(models.Model):
    data_val = models.DecimalField(decimal_places=20, max_digits=30)
    label = models.TimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'dashboard_sinedata'
