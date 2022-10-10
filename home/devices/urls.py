from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.devices_template, name='devices')
]