from django.db import models
from mdeditor.fields import MDTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = MDTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title