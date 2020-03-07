import json
from graphene_django.utils.testing import GraphQLTestCase
from cookbook.schema import schema
from .queries import queries


class TestIngredient(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['ingredients.json', ]
    # GraphQLTestCase not working

    def test_query(self):
        res = self.query(query=queries, op_name='getCategory')
        self.assertResponseNoErrors(res)


class TestUpdateCategory(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['ingredients.json', ]
    # GraphQLTestCase not working

    def test_update(self):
        res = self.query(query=queries,
                         op_name="updateCategory",
                         variables="{\"name\": \"teest\"}")
        self.assertResponseNoErrors(res)
