import graphene
from graphene_django import DjangoObjectType
from graphene_django_cud.mutations import DjangoCreateMutation

from recipe.models import Recipe, Ingredient, Product


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CreateProduct(DjangoCreateMutation):
    class Meta:
        model = Product

class Query:

    product = graphene.Field(ProductType,
                             id=graphene.Int(),
                             name=graphene.String(),
                             description=graphene.String()
                             )

    all_products = graphene.List(ProductType)

    ingredient = graphene.Field(IngredientType,
                                id=graphene.Int(),
                                measurement=graphene.String(),
                                amount=graphene.Float(),
                                product=graphene.Int()
                                )
    all_ingredients = graphene.List(IngredientType)

    recipe = graphene.Field(RecipeType,
                            id=graphene.Int(),
                            title=graphene.String(),
                            time_required=graphene.Int(),
                            difficulty=graphene.String(),
                            description=graphene.String(),
                            photo=graphene.String(),
                            )
    all_recipes = graphene.List(RecipeType)

    def resolve_all_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_recipe(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Recipe.objects.get(pk=id)

        return None

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Product.objects.get(pk=id)

        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        return None
