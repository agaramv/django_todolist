from time import timezone
from django.db import models

# Create your models here.
class TaskList(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  created = models.DateField()
  dueDate = models.DateTimeField()
  completed = models.BooleanField(default=False, blank=True)
  priority = models.IntegerField(blank=True) # Priority 1,2,3; 1 being the highest priority
  owner = models.ForeignKey('auth.User', related_name="tasklist", on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.title

class User(models.Model):
  username = models.CharField(max_length=30)
  tasks = TaskList