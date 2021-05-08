import graphene
import recipe.schema


class Query(recipe.schema.Query, graphene.ObjectType):
    pass

class MyMutations(graphene.ObjectType):
    create_product = recipe.schema.CreateProduct.Field()
    create_ingredient = recipe.schema.CreateIngredient.Field()
    create_recipe = recipe.schema.CreateRecipe.Field()

schema = graphene.Schema(query=Query, mutation=MyMutations)
