from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
# Create your models here.


class TaskListManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(created_by=user).order_by('name')


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    objects = TaskListManager()

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'

    def _str_(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    due_on = models.DateTimeField(default=datetime.now() + timedelta(days=2), blank=True)
    status = models.CharField(max_length=200, blank=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'created_by': self.created_by

        }

