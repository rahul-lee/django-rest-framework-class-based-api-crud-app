from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title
