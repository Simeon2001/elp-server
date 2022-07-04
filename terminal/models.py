from django.db import models
from django.contrib.auth.models import User

# Create your models here.title

class Command_Bank(models.Model):
    framework = models.CharField(max_length=100,blank=True)
    title = models.TextField(max_length=100,blank=False)
    command = models.CharField(max_length=100,blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class User_Command_Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    framework = models.CharField(max_length=100,blank=True)
    title = models.TextField(max_length=100,blank=False)
    command = models.CharField(max_length=100,blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
