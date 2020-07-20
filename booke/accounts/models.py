from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 


class Profile(models.Model):   
    # 유저 기본적으로 생성되긴 하지만 우리가 필요한 것들(목표량, 선호 장르 추가 위해 프로필 모델과 연결)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, blank=True)
    goal = models.CharField(max_length=20, blank=True)
    taste = models.CharField(max_length=20, blank=True)
    # goal(목표 페이지), taste(선호 장르)는 CharField 맞는지 확인해야함

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()
