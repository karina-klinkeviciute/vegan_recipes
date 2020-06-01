import graphene
from graphene_django import DjangoObjectType

from recipe.models import Recipe, RecipeIngredient, Ingredient


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe


class RecipeIngredientType(DjangoObjectType):
    class Meta:
        model = RecipeIngredient


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class Query:

    ingredient = graphene.Field(IngredientType,
                                id=graphene.Int(),
                                name=graphene.String(),
                                description=graphene.String()
                                )

    all_ingredients = graphene.List(IngredientType)

    recipe_ingredient = graphene.Field(RecipeIngredientType,
                                       id=graphene.Int(),
                                       measurement=graphene.String,
                                       amount=graphene.Int()
                                       )
    all_recipe_ingredients = graphene.List(RecipeIngredientType)

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

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_all_recipe_ingredients(self, info, **kwargs):
        return RecipeIngredient.objects.all()

    def resolve_recipe(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Recipe.objects.get(pk=id)

        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        return None

    def resolve_recipe_ingredient(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        return None
