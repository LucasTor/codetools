from django.test import TestCase

# Create your tests here.

class TestHome(TestCase):

    def testTitle(self):
        response = self.client.get('/')
        self.assertInHTML('Bem Vindo', response.content.decode())
    
    def testStatusCode(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
