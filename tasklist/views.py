from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskListSerializer
from .models import TaskList
# API Overview

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List' : '/task/all',
    'Create': '/task/create',
    'Update': '/task/update/<str:pk>',
    'Delete': '/task/delete/<str:pk>'
  }
  return Response(api_urls)

@api_view(['GET'])
def taskList(request):
  taskList = TaskList.objects.all()
  serializer = TaskListSerializer(taskList, many = True)
  return Response(serializer.data)