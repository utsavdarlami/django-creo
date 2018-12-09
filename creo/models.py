from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Testers(models.Model):
    user_name = models.CharField(max_length=264,unique=True)
    first_name  =  models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email_id =  models.EmailField(max_length=264,unique=True)
    def __str__(self):
        return self.user_name
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to ='profilepics',blank=True)
    def __str__(self):
        return self.user.username