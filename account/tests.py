from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestAccount(TestCase):

    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')
     
    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_dashboard_page(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/dashboard.html')

    def test_delete_button(self):
        response = self.client.get('/delete_button')
