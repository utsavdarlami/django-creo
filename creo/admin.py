from django.contrib import admin
from creo.models import UserProfileInfo,PostSubmission,CommentPost,Likes
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(PostSubmission)
admin.site.register(CommentPost)
admin.site.register(Likes)
admin.site.register(SavedPost)