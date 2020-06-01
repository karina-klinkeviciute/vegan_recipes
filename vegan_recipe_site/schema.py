import graphene
import recipe.schema


class Query(recipe.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)