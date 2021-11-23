from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save
from analyze.models import URLAnalyze
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    nickname = models.CharField(max_length=20,default="")
    bring = models.JSONField(null=True) #퍼올 url 담을 칼럼
    pick = models.ManyToManyField(URLAnalyze,related_name='picked',
                                  through='user_pick_url')
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class user_pick_url(models.Model): #다대다 관계를 위한 중개모델
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    url=models.ForeignKey(URLAnalyze,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)