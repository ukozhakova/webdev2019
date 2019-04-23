from django.shortcuts import render
from django.db import models
import json
from django.http import JsonResponse
from ..models import TaskList, Task
from django.views.decorators.csrf import csrf_exempt
from ..serializers import TaskSerializer, TaskListSerializer
# Create your views here.

@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        TaskLists = TaskList.objects.all()
        serializer = TaskListSerializer(TaskLists, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer(data = data)
        if serializer.is_valid():
            serializer.save() # create
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)

@csrf_exempt
def task_list_detail(request, pk):
    try:
        taskList= TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = TaskListSerializer(taskList)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance= taskList, data=data)
        if serializer.is_valid():
            serializer.save() #update
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        taskList.delete()
        return JsonResponse({}, status=204)


@csrf_exempt
def task_list_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)


@csrf_exempt
def task_list_task_detail(request, pk, pk2):
    try:
        task_list = TaskList.objects.get(id=pk)
        task = task_list.task_set.get(id=pk2)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskSerializer(instance=task, data=data)
        if serializer.is_valid():
            serializer.save()  # update
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({}, status=204)
