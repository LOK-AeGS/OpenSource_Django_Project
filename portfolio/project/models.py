from django.db import models
from login.models import User

# Create your models here.
class AllProject(models.Model):
    projectName = models.CharField(max_length=200)
    projectDate = models.DateTimeField('date published')
    projectUserName = models.ForeignKey(User,to_field='userId',on_delete=models.CASCADE, null=True)
    
class DetailProject(models.Model):
    projectId = models.ForeignKey(AllProject, on_delete=models.CASCADE)
    projectContent = models.CharField(max_length=1000)
    
class Reivew(models.Model):
    projectReviewStar = models.IntegerField()
    projectId = models.ForeignKey(AllProject, on_delete=models.CASCADE)
    userName = models.CharField(max_length=10) #사용자 이름
    projectReviewContent = models.CharField(max_length=1000)
