from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'day', 'time')
    list_display_links = ('id', 'user', 'day')
    search_fields = ('user', 'day')
    list_per_page = 10
