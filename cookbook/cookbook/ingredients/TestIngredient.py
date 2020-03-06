import json

from graphene_django.utils.testing import GraphQLTestCase
from cookbook.schema import schema


class TestIngredient(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['ingredients.json', ]
    # GraphQLTestCase not working

    def Xest_query(self):
        res = self.query(query='{allCategories{pageInfo {hasNextPage}}}'
                         # ,op_name='allCategories'
                         )
        self.assertResponseNoErrors(res)
