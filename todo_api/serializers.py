from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
            "user",
            # "created_at",
            # "updated_at",
            # "expires_at",
        ]
        # read_only_fields = ["id", "user", "created_at", "updated_at", "expires_at"]
