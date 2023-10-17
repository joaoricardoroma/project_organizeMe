from rest_framework.serializers import ModelSerializer
from .models import Record


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = ['created_at', 'id', 'task', 'task_description', 'email']