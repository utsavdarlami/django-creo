from django.urls import path
from . import views
urlpatterns = [
    path('users/',views.all_user,name="allusers"),
    path('profile/',views.profile,name="profile"),
    path('signout/',views.user_logout,name="user_logout"),
    path('createaccount/',views.create_user,name="createaccount"),
    path('',views.homecreo,name="homecreo"),
    path('photos/',views.allimage,name="allimage"),
    path('videos/',views.allvideo,name="allvideo"),
    path('audios/',views.allaudio,name="allaudio"),
    path('delete/<int:pk>',views.UserDeleteView.as_view(),name="deleteconfirm"),
    path('update/<int:pk>',views.UserUpdateView.as_view(),name="updateprofile"),
    path('post/',views.PostFormView.as_view(),name="post"),
    path('posts/<int:id>/',views.detailpost,name="detailpost"),
    path('<int:id>/comment/',views.addcomment,name="addcomment"),
    path('<int:id>/likes/',views.addlike,name="addlike"),
    path('portfolio/<str:publisher>/',views.artistdetail,name="artistdetail"),



]
