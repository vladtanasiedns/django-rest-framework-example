from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=500, null=False)
    completed = models.BooleanField(null=False)

    def __str__(self) -> str:
        return self.title