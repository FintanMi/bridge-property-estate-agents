from django.shortcuts import render, redirect
from .models import Appointment
from django.contrib import messages


def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        appointment_times = request.POST['appointment_times']
        appointment_day = request.POST['appointment_day']
        message = request.POST['message']

    return render(request, 'account/appointment.html')


def appointment_confirm(request):
    return render(request, 'account/appointment_confirm.html')
