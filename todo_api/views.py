from rest_framework import permissions
from rest_framework import generics
from todo.models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAdminUser
from django.utils import timezone
from datetime import timedelta

# class TaskList(generics.ListCreateAPIView):
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_superuser:
#             return Task.objects.all()
#         else:
#             return Task.objects.filter(user=user)

#     serializer_class = TaskSerializer

from django.contrib.auth.models import AnonymousUser


class TaskList(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user

        if isinstance(user, AnonymousUser):
            # Handle the case where the user is anonymous (not logged in)
            return Task.objects.none()

        if user.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(user=user)

    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    # Only Admin can update and destroy data
    permission_classes = [IsAdminUser]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


"""
# CreateAPIView
# ListAPIView
# RetrieveAPIView
# DestroyAPIView
# UpdateAPIView
# # ListCreateAPIView
# # RetrieveUpdateAPIView
# # RetrieveDestroyAPIView
# # RetrieveUpdateDestroyAPIView
"""


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        expires_at=timezone.now() + timedelta(minutes=5))


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
