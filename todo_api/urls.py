from django.urls import path
from .views import TaskList, TaskDetail

app_name = 'todo_api'

urlpatterns = [
    path('<int:pk>/', TaskDetail.as_view(), name='detailcreate'),
    path('', TaskList.as_view(), name='listcreate'),
]
