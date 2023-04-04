from django.db import models
import datetime


class SineData(models.Model):
    value = models.DecimalField(decimal_places=32, max_digits=32)
    label = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['-label']

    def get_data(self, start, end):
        self.start = datetime.time(start)
        self.end = datetime.time(end)
        self.data = SineData.objects.filter(label__gte=self.start, label__lte=self.end)
        return self.data
