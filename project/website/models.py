from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=200)
    task_description = models.TextField(default='Unplanned goal pussy')
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email}"
