from django.db import models
class Device(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=100)
    type = models.CharField(max_length=100)