from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestHelp(TestCase):
   
    def testStatusCodeAbout(self):
        response = self.client.get(reverse('help:about'))
        self.assertEquals(response.status_code, 200)

    def testStatusCodeContrib(self):
        response = self.client.get(reverse('help:contrib'))
        self.assertEquals(response.status_code, 200)
