from time import timezone
from django.db import models

# Create your models here.
class TaskList(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  created = models.DateField()
  dueDate = models.DateTimeField()