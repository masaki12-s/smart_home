from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home_template, name='home'),
    path('', views.device_template, name='device')
]