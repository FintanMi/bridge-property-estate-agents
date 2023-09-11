from django.urls import path
from . import views

urlpatterns = [
    path('appointment', views.appointment, name='appointment'),
    path('appointment_confirm', views.appointment_confirm, name='appointment_confirm'),
]
