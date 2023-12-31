from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length = 100)
    listing_id = models.IntegerField(blank = False, null=True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50)
    phone = models.CharField(max_length = 50)
    message = models.TextField(blank = True)
    contact_date = models.DateTimeField(default = datetime.now, blank = True)
    user_id = models.IntegerField(blank = True)

    def __str__(self):
        return self.name
