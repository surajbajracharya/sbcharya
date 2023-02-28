from django.db import models

class Websetting(models.Model):
    website_name = models.CharField(max_length=255)
    hero_title = models.CharField(max_length=255)
    hero_text = models.TextField()
    learning_title = models.CharField(max_length=255)
    work_title = models.CharField(max_length=255)
    contact_title = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
