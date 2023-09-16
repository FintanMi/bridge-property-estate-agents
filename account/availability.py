import datetime
from .models import Appointment

def check_availability(appointment_time):
    availability = []
    appointment = Appointment.objects.filter(appointment_time=appointment_time)
    for booking in appointment:
        if booking.appointment_time == appointment_time:
            availability.append(True)
        else:
            availability.append(False)
    return all(availability)