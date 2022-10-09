from django.shortcuts import render
#from . import models

def home_template(request):
    return render(request, 'home.html')



def log_template(request):
    return render(request, 'log.html')

