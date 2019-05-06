from ..models import TaskList, Task
from django.contrib.auth.models import User
from ..serializers import TaskListSerializer2, UserSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ..filters import TaskFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class TaskList2(generics.ListAPIView):
   queryset = TaskList.objects.all()
   serializer_class = TaskListSerializer2
   http_method_names = ['get']


class Lists(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields=('name',)

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2


class TasksFromList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = TaskFilter
    #filterset_fields = ('name', 'status',)
    search_fields = ('name', 'status')
    ordering_fields = ('name', 'status')
    ordering = ('name',)

    def get_queryset(self):
        try:
            t = TaskList.objects.get(id=self.kwargs['pk'])
        except TaskList.DoesNotExist:
            raise Http404
        queryset = t.tasks.all()
        # name = self.request.query_params.get('name', None)
        # status = self.request.query_params.get('status', None)
        # if name is not None and status is not None:
        #     queryset = queryset.filter(name=name).filter(status=status)
        return queryset
