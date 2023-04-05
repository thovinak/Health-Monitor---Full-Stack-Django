from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField()
    date_of_birth = models.DateField(auto_now=True)
