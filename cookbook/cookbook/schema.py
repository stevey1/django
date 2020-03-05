import graphene

import cookbook.ingredients.schema


class Query(cookbook.ingredients.schema.IngredientQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(cookbook.ingredients.schema.IngredientMutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
