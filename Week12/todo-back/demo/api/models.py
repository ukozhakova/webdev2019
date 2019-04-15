from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def _str_(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField(default=datetime.now() + timedelta(days=2))
    status = models.CharField(max_length=200, blank=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at': self.created_at,
            'due_on': self.due_on

        }
