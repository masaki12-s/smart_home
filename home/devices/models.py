from django.db import models

class Device(models.Model):
    deviceid = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    hubdeviceid = models.CharField(max_length=20)

