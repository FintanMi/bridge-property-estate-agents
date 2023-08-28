from django.db import models
from cloudinary.models import CloudinaryField

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    top_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.name
