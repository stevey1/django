import json

from graphene_django.utils.testing import GraphQLTestCase
from cookbook.schema import schema


class TestIngredient(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['ingredients.json', ]

    def test_query(self):
        res = self.query(query='''
             {
                allCategories {
                    pageInfo {
                        hasNextPage
                        startCursor
                    }
                }
            }
        ''')
        self.assertResponseNoErrors(res)
