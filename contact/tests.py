from django.test import TestCase
from .models import Contact
from django.urls import reverse


class TestContact(TestCase):
    def test_contact_model(self):
        contact = Contact.objects.count()
        self.assertEqual(contact, 0)
