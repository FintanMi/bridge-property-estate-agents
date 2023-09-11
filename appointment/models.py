from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from contact.models import Contact


APPOINTMENT_TIME = ((1, "9:30am - 10:30am"), (2, "11:00am - 12:00pm"),
(3, "12:30pm - 13:30pm"), (4, "14:00pm - 15:00pm"), (5, "15:30pm - 16:30pm"),
(6, "17:00pm - 18:00pm"))


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
    blank=True)
    name = models.CharField(max_length=50, null=True)
    day = models.DateField()
    time = models.IntegerField(choices=APPOINTMENT_TIME, default=1)

    def __str__(self):
        return f"{self.user.name} | day: {self.day} | time: {self.time}"
