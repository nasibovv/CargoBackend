from django.db import models

class News(models.Model):
    title = models.CharField(max_length=225)
    summary = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
