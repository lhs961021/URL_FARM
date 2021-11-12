from django.db import models

# Create your models here.

class URLAnalyze(models.Model):
    url= models.URLField(null=False, blank=False)
    title= models.TextField(null=True)
    content=models.TextField(null=True)
    