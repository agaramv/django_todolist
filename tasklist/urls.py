from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  path('task/all/', views.taskList, name="task-list"),
  
]