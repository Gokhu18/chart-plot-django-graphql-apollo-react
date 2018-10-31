from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphiql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('gql', csrf_exempt(GraphQLView.as_view(batch=True))),
]
