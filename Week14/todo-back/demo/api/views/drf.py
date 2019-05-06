from ..serializers import TaskSerializer, TaskListSerializer
from ..models import TaskList, Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def taskLists(request):
    if request.method == 'GET':
        taskLists = TaskList.objects.all()
        # json_lists=[l.to_json() for l in all_lists]
        ser = TaskListSerializer(taskLists, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        ser = TaskListSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def task_list_detail(request,pk):
    try:
        taskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser=TaskListSerializer(taskList)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        ser = TaskListSerializer(instance=taskList, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    elif request.method=='DELETE':
        taskList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def list_tasks(request, pk):
    try:
        taskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        tasks = taskList.tasks.all()
        ser = TaskSerializer(tasks, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        TaskSerializer.task_list = taskList
        ser = TaskSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors)

