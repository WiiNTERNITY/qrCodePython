from rest_framework import viewsets, filters
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from .serializers import *
from .models import *

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class ProfileViewSet(viewsets.ModelViewSet):
    # filter_backends = (DynamicSearchFilter,)
    queryset = Profile.objects.all()
    serializer_class =  ProfileSerializer