from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestLorem(TestCase):
   
    def testStatusCodeIpsum(self):
        response = self.client.get(reverse('lorem:ipsum'))
        self.assertEquals(response.status_code, 200)

    def testStatusCodePixel(self):
        response = self.client.get(reverse('lorem:pixel'))
        self.assertEquals(response.status_code, 200)

    def testStatusCodePixel64(self):
        response = self.client.get(reverse('lorem:pixel'), {'base64':'1'})
        self.assertEquals(response.status_code, 200)
        
    def testStatusCodePixelIndex(self):
        response = self.client.get(reverse('lorem:pixel-index'))
        self.assertEquals(response.status_code, 200)