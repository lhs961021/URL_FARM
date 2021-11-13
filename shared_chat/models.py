from django.db import models

# Create your models here.

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default="")
    description=models.TextField()
    participants=models.JSONField()
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
