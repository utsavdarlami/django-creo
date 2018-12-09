from django.urls import path
from . import views
urlpatterns = [
    path('users/',views.all_user,name="allusers"),
    path('profile/',views.profile,name="profile"),
    path('signout/',views.user_logout,name="user_logout"),
    path('createaccount/',views.create_user,name="createaccount"),
    path('home/',views.home,name="home"),
]
