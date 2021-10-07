from rest_framework import serializers
from django_rest_tutorial.models.Task import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed']

    def create(self, validated_data):
        task = Task(
            title = validated_data['title'],
            completed = validated_data['completed']
        )
        task.save()
        return task