from django.test import TestCase
#from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from snippets.models import Snippet 
from django.contrib.auth.models import User, Group

# Create your tests here.
class test_snippets(TestCase):
    #def __init__(self,*args):
    @classmethod
    def setUpClass(cls):
        cls.client = APIClient()
        user=User.objects.create_superuser(username='steve',email='tst@hotmail.com', is_staff=True)
        Snippet.objects.create(title="title",code="code", owner=user)
        cls.client.force_authenticate(user=user)

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_get_snippet_detail(self):
        r= test_snippets.client.get('/snippets/1/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "linenos",status_code=200)

    def test_get_snippets(self):
        r= test_snippets.client.get('/snippets/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r,'id',count = 1, status_code=200)
    
    def test_post_snippets(self):
        #client.auth = HTTPBasicAuth('user', 'pass')
        #self.client.login(username='steve', password='')
        r= test_snippets.client.post('/snippets/',{'title': 'title2','code':'code2'}, format='json')
        self.assertEqual(r.status_code, 201)

    def test_patch_snippets(self):
        r= test_snippets.client.patch('/snippets/1/',{'title': 'titlepatch'}, format='json')
        self.assertEqual(r.status_code, 200)
    def test_put_snippets(self):
        r= test_snippets.client.put('/snippets/1/',{'title': 'titleput','code':'codeput'}, format='json')
        self.assertEqual(r.status_code, 200)

    def test_head_snippets(self):
        r= test_snippets.client.head('/snippets/')
        print(r.data)
        self.assertEqual(r.status_code, 200)