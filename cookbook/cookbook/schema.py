from graphene import ObjectType, Schema, Field

from cookbook.ingredients.schema import IngredientQuery, IngredientMutation
from cookbook.spacex.schema import SpacexQuery


class Query(IngredientQuery, SpacexQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(IngredientMutation, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query, mutation=Mutation)
