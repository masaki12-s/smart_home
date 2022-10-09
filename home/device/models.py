from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255)
    # id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

