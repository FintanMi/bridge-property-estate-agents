from django.contrib import admin
from .models import Realtor

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'photo',
        'description',
        'phone',
        'email',
        'top_seller',
    )
    
