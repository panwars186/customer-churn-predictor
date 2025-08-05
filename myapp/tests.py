from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_homepage_status_code(self):
        res= self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test2(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp,"Hello world from Django and Jenknins")