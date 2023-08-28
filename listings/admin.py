from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'estate_agent',
        'title',
        'address',
        'town',
        'province',
        'description',
        'price',
        'bedrooms',
        'bathrooms',
        'sqm',
        'photo',
        'is_published',
        'list_date',
    )
    list_display_links = ('title',)
    list_filter = ('estate_agent',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'town', 'province', 'price')
    list_per_page = 10
