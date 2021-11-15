from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default="",null=True)
    description=models.TextField(null=True)
    participants=models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
