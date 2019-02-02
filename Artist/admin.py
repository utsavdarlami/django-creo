from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Artist.models import UserProfileInfo,SavedPost
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(SavedPost)