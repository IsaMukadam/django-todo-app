from django.db import models
from django.utils import timezone


class Todo(models.Model):
    """
    Represents a single to-do item in the application.

    Fields:
        title (CharField): A short title for the task.
        details (TextField): A detailed description of the task.
        date (DateTimeField): The timestamp when the task was created.

    the __str__ method returns the title of the task for easier identification
    in the admin interfaces and querysets. 
    """
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

