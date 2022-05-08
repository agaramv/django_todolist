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
    'View-Task': '/task/view/<str:pk>',
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

"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskView(request, id):
  print(request," ID: ",id)
  task = TaskList.objects.get(id=id)
  serializer = TaskListSerializer(task, many = False)
  print(serializer)
  return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request, id):
  task = TaskList.objects.get(id=id)
  serializer = TaskListSerializer(instance=task, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)