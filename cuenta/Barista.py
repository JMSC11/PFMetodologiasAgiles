from django.contrib.auth.models import User
from django.db import models

class Barista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isBarista = True
def __str__(self):
    user = self.user
    username = user.username
    return f"{username}"