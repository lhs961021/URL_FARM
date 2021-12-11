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
    taken= models.ManyToManyField(User,related_name='brought',
                                 through='url_taken_by_user') #퍼간거
    category = models.CharField(max_length=10,null=True)
    keyword = models.JSONField(null=True)
    # image = models.ImageField(upload_to="cloud/",null=True,blank=True)
    # 이미지랑 요약본이랑 주요 키워드 정도도 추가해야함, 메모모델도
    
class url_taken_by_user(models.Model): #다대다 관계를 위한 중개모델
    urlanalyze=models.ForeignKey(URLAnalyze,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    