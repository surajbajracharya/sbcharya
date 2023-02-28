from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="work/")
    content = models.TextField()
    reference = models.CharField(max_length=255)