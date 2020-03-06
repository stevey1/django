import json

from graphene_django.utils.testing import GraphQLTestCase
from cookbook.schema import schema


class TestIngredient(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['ingredients.json', ]
    # GraphQLTestCase not working

    def test_query(self):
        res = self.query(query='''query getCategory {
            allCategories{
                pageInfo {
                    hasNextPage
                    }
                }
            } 
        ''', op_name='getCategory'
                         )
        self.assertResponseNoErrors(res)


class TestUpdateCategory(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['ingredients.json', ]
    # GraphQLTestCase not working

    def test_update(self):
        res = self.query(query='''
           mutation myMutation($name: String!) {
                updateCategory(name: $name) {
                    category {
                        id
                        name
                    }
                }
            }
            ''', variables="{\"name\": \"test\"}"

                         )
        self.assertResponseNoErrors(res)
