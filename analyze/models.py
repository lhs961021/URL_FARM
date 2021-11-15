from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class URLAnalyze(models.Model):
    url= models.URLField(null=False, blank=False)
    title= models.TextField(null=True)
    content=models.TextField(null=True)
    check=models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    