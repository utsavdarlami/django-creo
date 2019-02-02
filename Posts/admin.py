from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Posts.models import PostSubmission,CommentPost,Likes
# Register your models here.
admin.site.register(PostSubmission)
admin.site.register(CommentPost)
admin.site.register(Likes)
