from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    task = models.CharField(max_length=700)
    tag = models.IntegerField(auto_created=True)

    class Meta():
        ordering = ('-tag',)
    def ___str__(self):
        return self.task