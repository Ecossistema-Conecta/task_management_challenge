from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projects/', ListProjectView.as_view(), name='project_list'),
    path('projects/create/', CreateProjectView.as_view(), name='create_project'),
    path('projects/<int:pk>/', DetailProjectView.as_view(), name='project_detail'),

    path('tasks/<int:project_id>/', ListTaskView.as_view(), name='task_list'),
    path('tasks/create/', CreateTaskView.as_view(), name='create_task'),
]
