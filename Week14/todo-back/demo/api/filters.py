from django_filters import rest_framework as filters
from .models import Task


class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    status = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Task
        fields = ('name', 'status')


