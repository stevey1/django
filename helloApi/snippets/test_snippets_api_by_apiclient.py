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
        user=User.objects.create_superuser(username='test_snippets',email='test@hotmail.com', is_staff=True)
        Snippet.objects.create(title="title",code="code", owner=user)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        user = User.objects.get(username='test_snippets')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def tearDown(self):
        pass

    def test_get_root(self):
        self.client.force_authenticate(user=None)
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        #self.assertContains(r,'snippets:',count = 2, status_code=200)

    def test_head_snippets(self):
        res = self.client.head('/snippets/')
        self.assertEqual(res.status_code, 200)
    
    def test_get_snippets(self):
        res = self.client.get('/snippets/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res,'id',count = 1, status_code=200)
    
    def test_post_snippets(self):
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user=user)
        #client.auth = HTTPBasicAuth('user', 'pass')
        #self.client.login(username='steve', password='')
        res = self.client.post('/snippets/',{'title': 'title2','code':'code2'}, format='json')
        self.assertEqual(res.status_code, 201)

    def test_get_snippet_detail(self):
        res = self.client.get('/snippets/1/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "linenos",status_code=200)

    def test_patch_snippet_detail(self):
        #user = User.objects.get(username='test_snippets')
        #self.client.force_authenticate(user=user)
        res = self.client.patch('/snippets/1/', {'title': 'titlepatch'}, format='json')
        self.assertEqual(res.status_code, 200)

    def test_put_snippet_detail(self):
        res = self.client.put('/snippets/1/', {'title': 'titleput','code':'codeput'}, format='json')
        self.assertEqual(res.status_code, 200)

        