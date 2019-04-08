from django.shortcuts import render
from django.db import models
from django.http import JsonResponse
from api.models import TaskList
# Create your views here.


def task_lists(request):
    TaskLists= TaskList.objects.all()
    json_categories = [tl.to_json() for tl in TaskLists]
    return JsonResponse(json_categories, safe=False)


def task_list_detail(request, pk):
    try:
        taskList= TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(taskList.to_json())


def task_list_tasks(request, pk):
    try:
        task_list= TaskList.objects.get(id= pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)}, safe=False)
    tasks= task_list.task_set.all()
    json_tasks= [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)
