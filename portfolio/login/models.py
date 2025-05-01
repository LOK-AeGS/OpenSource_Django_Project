from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=10)
    userId = models.CharField(max_length=10, unique=True)
    userPassword = models.CharField(max_length=10)

class AdminUser(models.Model):
    userName = models.CharField(max_length=10)
    userId = models.CharField(max_length=10)
    userPassword = models.CharField(max_length=10)

# Create your models here.
