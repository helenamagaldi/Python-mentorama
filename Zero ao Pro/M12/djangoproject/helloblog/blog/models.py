from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)