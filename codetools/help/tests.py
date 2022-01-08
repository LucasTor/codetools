from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestHelp(TestCase):
   
    def testStatusCode(self):
        response = self.client.get(reverse('help:about'))
        self.assertEquals(response.status_code, 200)
