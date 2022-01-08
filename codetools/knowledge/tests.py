from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestKnowledge(TestCase):
   
    def testStatusCodeApis(self):
        response = self.client.get(reverse('knowledge:apis'))
        self.assertEquals(response.status_code, 200)

    def testStatusCodeOpenSource(self):
        response = self.client.get(reverse('knowledge:open-source-tools'))
        self.assertEquals(response.status_code, 200)