# Generated by Django 3.2.14 on 2022-08-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_task_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dateToComplete',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
