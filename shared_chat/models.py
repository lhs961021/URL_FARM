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
    #참가자를 json꼴로 받았는데 생각해보니 다대다필드 써서해도됐음. 오히려 그게 더 맞았을듯 개인정보가 수정되더라도 변경될거니까 
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