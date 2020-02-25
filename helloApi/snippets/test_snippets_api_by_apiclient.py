from django.test import TestCase
#from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from snippets.models import Snippet 
from django.contrib.auth.models import User, Group

# Create your tests here.
class test_snippets(TestCase):
    @classmethod
    def setUpClass(cls):
        client = APIClient()
        user=User.objects.create_superuser(username='steve',email='tst@hotmail.com', password='password222',is_superuser=True, is_staff=True)
        print(user.id)
        Snippet.objects.create(title="title",code="code", owner=user)
        client.force_authenticate(user=user)

    @classmethod
    def tearDownClass(cls):
        pass
    #def setUp(self):
    # def tearDown(self):

    def test_get_snippet_detail(self):
        r= self.client.get('/snippets/1/')
        print(r.data)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "linenos",status_code=200)

    def test_get_snippets(self):
        r= self.client.get('/snippets/')
        print(r.data)
        self.assertEqual(r.status_code, 200)
        #self.assertContains(r,count = 1, status_code=200)
    def test_post_snippets(self):
                
        #client.auth = HTTPBasicAuth('user', 'pass')
        #self.client.login(username='steve', password='')
        r= self.client.post('/snippets/',{'title': 'title2','code':'code2'}, format='json')
        print(r.data)
        self.assertEqual(r.status_code, 200)
       #self.assertContains(r,count = 1, status_code=200)


