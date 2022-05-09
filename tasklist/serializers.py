from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TaskList

class TaskListSerializer(serializers.ModelSerializer):
  owner  = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = TaskList
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  # tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=TaskList.objects.all())

  class Meta:
    model = User
    fields = ['id','username']