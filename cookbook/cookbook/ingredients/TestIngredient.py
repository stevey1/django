import json

from graphene_django.utils.testing import GraphQLTestCase
from cookbook.schema import schema


class TestIngredient(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_query(self):
        res = self.query('''
            query myModel {
                allCategories {
                    pageInfo {
                        hasNextPage
                        startCursor
                    }
                }
            }
        ''', op_name='myModel2')
        content = json.loads(res.content)
        self.assertResponseNoErrors(res)
