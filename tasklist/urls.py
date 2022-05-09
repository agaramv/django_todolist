from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="TODO APP API",
#         default_version='v1',
#         description="",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny),
# )

urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  path('task/all/', views.TaskListAll.as_view(), name="task-list"),
  # path('task/view/<str:id>/', views.taskView, name="task-view"),
  # path('task/update/<str:id>/', views.taskUpdate, name="task-update"),
  # path('task/create/', views.taskCreate, name="task-create"),
  # path('task/delete/<str:pk>/', views.taskDelete, name="task-delete"),
  # path('task/universal/<str:pk>/', views.TaskListUniversal.as_view(), name="task-univesal")
  path('task/<str:pk>', views.TaskListDetail.as_view(), name="task-detail"),
  path('users/', views.UserList.as_view()),
  path('users/<int:pk>', views.UserDetail.as_view()),

  
]

urlpatterns = format_suffix_patterns(urlpatterns)
