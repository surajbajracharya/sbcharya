from django.db import models

class Timeline(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    content = models.TextField()