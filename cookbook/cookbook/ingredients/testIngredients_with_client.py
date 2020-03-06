from django.test import TestCase
#from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group

# Create your tests here.


class test_category(TestCase):
    # def __init__(self,*args):
    fixtures = ['ingredients.json', ]

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get_snippet_detail(self):
        res = self.client.get('/graphql',{"query":"{allCategories{pageInfo{hasNextPage}}}"}, format='json')
        self.assertEqual(res.status_code, 200)
