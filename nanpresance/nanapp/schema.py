import graphene
from .models import *
from graphene import relay, ObjectType, Connection, Node, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django_filters import FilterSet, OrderingFilter
from django.contrib.auth.models import User

class ExtendedConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)

# class UserNode(DjangoObjectType):
#     class Meta:
#         model = User
         
#         filter_fields = ['first_name','last_name','email']
          
        
      
#         interfaces = (relay.Node, )
#         connection_class = ExtendedConnection
class QrcodeNode(DjangoObjectType):
    class Meta:
        fields = "__all__"
        model = Qrcode

        filter_fields = ['jours']
        
        order_by = OrderingFilter(
            fields=(
                ('created_at','created_at'),
          
            )
        )
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection



class Query(ObjectType):
    Qrcode = relay.Node.Field(QrcodeNode)
    all_Qrcode = DjangoFilterConnectionField(QrcodeNode)