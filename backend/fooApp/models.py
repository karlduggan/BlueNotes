from django.db import models

# Create your models here.
# Models are how a user interacts with the database

class foo(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    data = models.IntegerField()
    def __str__(self):
        return self.name