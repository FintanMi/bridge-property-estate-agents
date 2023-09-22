from django.test import TestCase
from .models import Listing
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestListing(TestCase):


    def setUp(self):
        username = "admin"
        password = "theposhci"
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            username = username,
            password = password,
            is_superuser = True,
            is_staff = True
        )
        logged_in = self.client.login(username = username, password = password)
        self.assertTrue(logged_in)


    def test_listings(self):
        response = self.client.get('/listings/')
        self.assertEqual(response.status_code, 200)


    def test_search(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/search.html')
