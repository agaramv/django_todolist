from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  path('task/all/', views.taskList, name="task-list"),
  path('task/view/<str:id>/', views.taskView, name="task-view"),
  path('task/update/<str:id>/', views.taskUpdate, name="task-update"),
]