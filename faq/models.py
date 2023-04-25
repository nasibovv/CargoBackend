from django.db import models

class FAQ_category(models.Model):
    title = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FAQ(models.Model):
    category = models.ForeignKey(FAQ_category, on_delete=models.CASCADE)
    question = models.CharField(max_length=225)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    row_status = models.IntegerField(default=1)