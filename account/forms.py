from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from listings.models import Listing


class StaffListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'