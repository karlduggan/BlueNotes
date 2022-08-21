
from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    createdBy = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, default='None')
    timestamp = models.CharField(max_length=100, default="None")
    # Project Stats can be entered later
    def __str__(self):
        return self.title

class Ticket(models.Model):
    projectID = models.ForeignKey(Project, default=None, on_delete=models.CASCADE, null=True, blank=True, related_name = "projectID")
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
    ticketID = models.ForeignKey(Ticket, default=None, on_delete=models.CASCADE, null=False, blank=True, related_name="ticketID")
    #thumb = models.ImageField(default='default.png', blank=True)
    comment = models.TextField(max_length=1000, default='None')
    createdBy = models.CharField(max_length=100, default="None")
    
    def snippet(self):
        return self.comment[:50] + '...'

"""
        https://www.youtube.com/watch?v=zJWhizYFKP0&ab_channel=TheNetNinja
"""