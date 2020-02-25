from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from snippets.models import Snippet 
from django.contrib.auth.models import User, Group

# Create your tests here.
class test_snippets(TestCase):
    def setUp(self):
        user=User.objects.create_superuser(username='steve')
        Snippet.objects.create(title="title",code="code", owner=user)

    def test_get_snippet_detail(self):
        client = APIClient()
        r= client.get('/snippets/1/')
        print(r.data)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "linenos",status_code=200)

    def test_get_snippets(self):
        client = APIClient()
        r= client.get('/snippets/')
        print(r.data)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r,count = 1, status_code=200)


