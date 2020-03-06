from django.test import TestCase
# from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from .queries import queries

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

    def test_get_allCategories_detail(self):
        res = self.client.get(
            '/graphql',
            {"query": queries, "operationName": "getCategory"},
            format='json')
        self.assertEqual(res.status_code, 200)

    def test_mutate_categoryByForm(self):
        res = self.client.post(
            '/graphql', data={"query": queries, "operationName": "updateCategoryByForm"}, format='json')
        self.assertEqual(res.status_code, 200)

    def test_mutate_categoryByForm_through_input(self):
        updateCategoryByForm = '''
            mutation updateCategoryByFormInput($input: UpdateCategoryByFormInput!) {
                            updateCategoryByForm(input: $input){
                                category {
                                    id
                                    name
                                }
                            }
                        }
                        '''
        res = self.client.post(
            '/graphql',
            data={"query": updateCategoryByForm, "operationName": "updateCategoryByFormInput",
                                                 "variables": "{\"input\":{\"name\": \"someValue\"}}"}, format='json')
        self.assertEqual(res.status_code, 200)


def test_mutate_category_through_variable(self):
    res = self.client.post(
        '/graphql',
        data={"query": queries,              "operationName": "updateCategory", "variables": "{\"name\": \"someValue\"}"}, format='json')
    self.assertEqual(res.status_code, 200)
