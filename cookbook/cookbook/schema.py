from graphene import ObjectType, Schema

from cookbook.ingredients.schema import IngredientQuery, IngredientMutation


class Query(IngredientQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(IngredientMutation, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query, mutation=Mutation)
