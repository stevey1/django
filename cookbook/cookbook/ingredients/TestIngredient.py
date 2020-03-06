import json
from graphene_django.utils.testing import GraphQLTestCase
from cookbook.schema import schema


class TestIngredient(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['ingredients.json', ]
    # GraphQLTestCase not working

    def test_query(self):
        getCategory = '''
        query getCategory {
            allCategories{
                pageInfo {
                    hasNextPage
                    }
                }
            } 
        '''
        res = self.query(query=getCategory, op_name='getCategory')
        self.assertResponseNoErrors(res)


class TestUpdateCategory(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['ingredients.json', ]
    # GraphQLTestCase not working

    def test_update(self):
        updateCategory = '''
           mutation myMutation($name: String!) {
                updateCategory(name: $name) {
                    category {
                        id
                        name
                    }
                }
            }
            '''
        res = self.query(query=updateCategory,
                         variables="{\"name\": \"test\"}")
        self.assertResponseNoErrors(res)
