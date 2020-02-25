from django.test import TestCase
#from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from snippets.models import Snippet 
from django.contrib.auth.models import User, Group

# Create your tests here.
class test_api_auth(TestCase):
    #def __init__(self,*args):
    @classmethod
    def setUpClass(cls):
        user=User.objects.create_superuser(username='test-login',email='login@hotmail.com', password='password2', is_staff=True)

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_get_login(self):
        res= self.client.get('/api-auth/login/')
        self.assertEqual(res.status_code, 200)
    
    def test_post_login(self):
        res= self.client.post('/api-auth/login/',{'username':'test-login','password':'password2'})
        self.assertEqual(res.status_code, 302)
        self.assertIsNotNone(res.cookies["sessionid"])
        self.assertIsNotNone(res.cookies["csrftoken"])
