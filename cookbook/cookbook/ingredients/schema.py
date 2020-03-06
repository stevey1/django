import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import CategoryForm
from cookbook.ingredients.models import Category, Ingredient
from graphene_django.debug import DjangoDebug

# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name']
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.prefetch_related('ingredients')


'''
    @classmethod
    def get_node(cls, info, id):
        return None
    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(name="test")
'''


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
        interfaces = (relay.Node,)

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.select_related('category')


class IngredientQuery(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
    debug = graphene.Field(DjangoDebug, name='_debug')


'''
    def resolve_all_categories(self, info):
        return Category.objects.none()
'''


class UpdateCategory(graphene.Mutation):
    category = graphene.Field(CategoryNode)
    debug = graphene.Field(DjangoDebug, name='_debug')

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


class UpdateCategoryByRelay(relay.ClientIDMutation):
    category = graphene.Field(CategoryNode)

    class Input:
        name = graphene.String(required=True)
        id = graphene.ID()

    # def mutate_and_get_payload(self, info, name, id=None):
    # @classmethod
    # def mutate_and_get_payload(cls, root, info, name, id=None):
    @staticmethod
    def mutate_and_get_payload(root, info, name, id=None):
        if(id):
            category = Category.objects.get(
                pk=graphene.Node.from_global_id(id)[1])
        else:
            category = Category()
        category.name = name
        category.save()
        return UpdateCategoryByRelay(category=category)


class UpdateCategoryByForm(DjangoModelFormMutation):
    category = graphene.Field(CategoryNode)

    class Meta:
        form_class = CategoryForm
        input_field_name = 'data'
        #return_field_name = 'my_category'


class IngredientMutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    update_category_by_form = UpdateCategoryByForm.Field()
    update_category_by_relay = UpdateCategoryByRelay.Field()
