from rest_framework import serializers
from .models import Task, TaskList
from django.contrib.auth.models import User


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        taskList = TaskList(**validated_data)
        taskList.save()
        return taskList

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True)
    # created_at = serializers.DateTimeField(required=False)
    # due_on = serializers.DateTimeField(required=False)
    # status = serializers.CharField(required=True)
    # #task_list = TaskListSerializer(write_only=True)
    # created_by = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_by', 'created_at', 'due_on', 'status')
        # fields = '_all_'


class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    tasks= TaskSerializer(many=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', 'tasks')

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        task_List = TaskList.objects.create(**validated_data)
        arr = [Task(task_list=task_List, **task) for task in tasks]
        Task.objects.bulk_create(arr)
        return task_List
