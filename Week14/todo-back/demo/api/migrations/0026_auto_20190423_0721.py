# Generated by Django 2.2 on 2019-04-23 01:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190423_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 23, 7, 21, 38, 373767)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 7, 21, 38, 373767)),
        ),
    ]