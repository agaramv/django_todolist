from time import timezone
from django.db import models


class TaskList(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  created = models.DateField()
  dueDate = models.DateTimeField()
  # Marks whether a task is complete
  completed = models.BooleanField(default=False, blank=True)
  # Priority 1,2,3; 1 being the highest priority
  priority = models.IntegerField(blank=True) 
  # Added owner to the task item using the django user model
  owner = models.ForeignKey('auth.User', related_name="tasklist", on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.title