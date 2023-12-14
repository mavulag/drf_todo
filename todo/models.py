from django.db import models

# Create your models here.
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class Task(models.Model):

    class TaskObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all()

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todo_tasks')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    objects = models.Manager()  # default manager
    taskobjects = TaskObjects()  # custom manager

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Set expires_at to current time plus 5 minutes when creating or updating
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(minutes=5)
        super().save(*args, **kwargs)
