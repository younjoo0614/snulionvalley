from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 


class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    realname = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    ordinal = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()
