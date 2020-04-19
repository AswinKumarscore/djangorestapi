from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.TextField()
    password = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)