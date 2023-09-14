from django.test import TestCase
from .models import Contact
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    def setUp(self):
        username = 'admin'
        password = 'theposhci'
        user_model = get_user_model()

        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True,
            is_staff=True
        )

        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)
