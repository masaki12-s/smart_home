from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.device_template, name='device')
]