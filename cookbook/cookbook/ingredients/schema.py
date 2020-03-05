import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cookbook.ingredients.models import Category, Ingredient

# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name']
        interfaces = (relay.Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


class UpdateCategory(graphene.Mutation):
    category = graphene.Field(CategoryNode)

    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    def mutate(self, info, name, id=None):
        if (id):
            db_id = graphene.Node.from_global_id(id)[1]
            category = Category.objects.get(pk=db_id)
        else:
            category = Category()
        category.name = name
        category.save()
        return UpdateCategory(category=category)


class IngredientQuery(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)


class IngredientMutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
