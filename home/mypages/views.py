from django.shortcuts import render
#from . import models

def home_template(request):
    return render(request, 'home.html')

def device_template(request):
    return render(request, 'device.html')