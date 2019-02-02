from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# User Profile ,User ,Post,comments post  and   posts likes model declared 
class PostSubmission(models.Model):
    POST_CHOICES = (
   (0, 'Image'),
   (1, 'Video'),
   (2,'Audio')
   )   
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.FileField(upload_to ='posts', blank=True)
    post_type = models.IntegerField(choices=POST_CHOICES)
    publisher = models.ForeignKey(User,on_delete=models.CASCADE,)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class CommentPost(models.Model):
    title = models.ForeignKey(PostSubmission,on_delete=models.CASCADE,)
    publisher = models.ForeignKey(User,on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    comment  = models.CharField(max_length=500)
    def __str__(self):
        return str(self.title)

class Likes(models.Model):
    post = models.ForeignKey(PostSubmission,on_delete=models.CASCADE,)
    publisher = models.ForeignKey(User,on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    like  = models.BooleanField()
    def __str__(self):
        return str(self.publisher)


