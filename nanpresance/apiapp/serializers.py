from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from nanapp.models import *
from django.contrib.auth.models import User

class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
  
    
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 2

class ProfileSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    user = UserSerializer
    
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1