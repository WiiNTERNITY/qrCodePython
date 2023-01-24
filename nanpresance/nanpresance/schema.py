import graphene

import nanapp.schema


class Query(nanapp.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
# class Mutation(quizz_app.schema.RelayMutation,graphene.ObjectType):
#     pass

schema = graphene.Schema(query=Query,)