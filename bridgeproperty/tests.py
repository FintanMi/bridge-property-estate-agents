from django.test import TestCase


class TestViews(TestCase):

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bridgeproperty/index.html')

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bridgeproperty/about.html')
