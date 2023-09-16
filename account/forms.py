from django import forms


class AppointmentForm(forms.Form):
    booking_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])