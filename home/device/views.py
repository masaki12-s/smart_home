from django.shortcuts import render
from . import models

def device_template(request):
    context = {"name" : "test"}# }
    return render(request, 'device.html', context)

