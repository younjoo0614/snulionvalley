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
    # select로 2000 선택하면 우리가 views에서 goal에 숫자로(integer로) 2000 넣어주는 것인지 확인
    follows = models.ManyToManyField('self', through = 'Follow', blank=True, related_name = 'followed', symmetrical=False)
    #친구 지금은 팔로우 관계라 symetrical-False로 해놨는데 어떤 방식일지 정해야 함
    already_read=models.IntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()


class Follow(models.Model):
    follow=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followed_by")
    followed_by=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="follow")

    def __str__(self):
        return '{} follows {}'.format(self.followed_by,self.follow)

