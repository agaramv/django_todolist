from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TaskList

class TaskListSerializer(serializers.ModelSerializer):
  # Made the owner field to a readonly field
  owner  = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = TaskList
    fields = '__all__'

# Created a User serializer based on the django auth models
class UserSerializer(serializers.ModelSerializer):
  # Added tasks by user to the user model
  # tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=TaskList.objects.all())

  class Meta:
    model = User
    # Explicitly include the fields when addings tasks bc tasks weren't part of the original model
    # fields = ['id','username','tasks']
    fields = ['id','username']