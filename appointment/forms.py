from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'day', 'time']
        appointment_date = forms.DateField()
        labels = {
            'name': 'Name',
            'day': 'Day',
            'time': 'Time',
        }

    def check(self):
        day = self.cleaned_data['day']
        time = self.cleaned_data['time']

        appointment_request = Appointment.objects.filter(day=day, time=time)

        if day < datetime.today().date():
            raise ValidationError('Pick another date')
        if not appointment_request:
            raise ValidationError('No slot available at this date and time')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['day'].widget.attrs['class'] = 'date'