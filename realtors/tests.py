from django.test import TestCase
from .models import Realtor


class TestRealtor(TestCase):
    def test_realtor(self):
        realtor = Realtor.objects.count()
        self.assertEqual(realtor, 0)
        