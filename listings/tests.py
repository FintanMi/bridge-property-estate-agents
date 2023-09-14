from django.test import TestCase
from .models import Listing
from django.contrib.auth import get_user_model


class TestListing(TestCase):

    def setUp(self):
        username = "admin"
        password = "theposhci"
        user_model = get_user_model()
        
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True,
            is_staff=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

    def test_listing(self):
        response = self.client.get('templates/listings/listings.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/listings/listings.html')
