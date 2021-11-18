from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from analyze.models import URLAnalyze
# Create your models here.

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default="",null=True)
    description=models.TextField(null=True)
    participants=models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="chats")
    url=models.ForeignKey(URLAnalyze,on_delete=CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)