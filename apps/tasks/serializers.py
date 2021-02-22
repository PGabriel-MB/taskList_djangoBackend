from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task 
        fields = '__all__'
        extra_kwargs = {
            'task_name': {'required': False},
            'description': {'required': False},
            'completed': {'required': False},
            'task_status': {'required': False}
        }