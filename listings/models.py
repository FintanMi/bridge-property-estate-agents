from django.db import models
from realtors.models import Realtor
from cloudinary.models import CloudinaryField
from datetime import datetime


class Listing(models.Model):
    estate_agent = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sqm = models.IntegerField()
    photo = CloudinaryField('image', default='placeholder')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

