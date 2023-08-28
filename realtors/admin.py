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
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10

