from django.test import TestCase
#from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from snippets.models import Snippet 
from django.contrib.auth.models import User, Group

# Create your tests here.
class test_token_api_auth(TestCase):
    #def __init__(self,*args):
    @classmethod
    def setUpClass(cls):
        User.objects.create_superuser(username='test-token',email='token@hotmail.com', password='password2', is_staff=True)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        user = User.objects.get(username='test-token')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def tearDown(self):
        pass

    def test_post_token(self):
        res = self.client.post('/api-token-auth/', {'username':'test-token','email':'token@hotmail.com', 'password':'password2', 'is_staff': True})
        self.assertEqual(res.status_code, 200)
        self.assertTrue('token' in res.data)
