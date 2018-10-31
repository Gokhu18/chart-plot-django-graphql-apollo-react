import graphene

import chart_app.schema

class Queries(
    chart_app.schema.Query,
    graphene.ObjectType
):
    dummy = graphene.String()


schema = graphene.Schema(query=Queries)