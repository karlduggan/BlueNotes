from tkinter import CASCADE
from django.db import models
#from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    projectID = models.ForeignKey(Project, default=None, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, default='None')
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='ToDo')
    timestamp = models.CharField(max_length=100, default="None")
    priority = models.CharField(max_length=10, default="None")
    dateToComplete = models.CharField(max_length=100, default=False)
    createdBy = models.CharField(max_length=100, default="None")
    
    def __str__(self):
        return self.title
#Foreign key must reference a primary key or unique constraint

        
class Comment(models.Model):
    ticketID = models.ForeignKey(Task, default=None, on_delete=models.CASCADE, null=True, blank=True)
    thumb = models.ImageField(default='default.png', blank=True)
    comment = models.TextField(max_length=1000, default='None')
    
    def __str__(self):
        return self.title
    def snippet(self):
        return self.comment[:50] + '...'

"""
        https://www.youtube.com/watch?v=zJWhizYFKP0&ab_channel=TheNetNinja
"""