from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class URLAnalyze(models.Model):
    url= models.URLField(null=False, blank=False)
    title= models.TextField(null=True)
    content=models.TextField(null=True)
    check=models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    # 이미지랑 요약본이랑 주요 키워드 정도도 추가해야함, 메모모델도