from django.db import models



class Info(models.Model):
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    message = models.TextField()