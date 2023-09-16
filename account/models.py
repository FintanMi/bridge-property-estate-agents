from django.db import models
from django.conf import settings

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has made an appointment for {self.appointment_time}'
