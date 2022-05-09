from django.contrib import admin

# Registered the Tasklist model bc it isn't automatically added
from .models import TaskList
admin.site.register(TaskList)
# Add additional Models 