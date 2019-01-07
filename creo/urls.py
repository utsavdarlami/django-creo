from django.urls import path
from . import views
#url request which is mapped to  functions of views.py( inside creo folder)
urlpatterns = [
    path('users/',views.all_user,name="allusers"),#calls all_user function of views.py
    path('profile/',views.profile,name="profile"),#calls profile function of views.py
    path('signout/',views.user_logout,name="user_logout"),#calls user_logout function of views.py
    path('createaccount/',views.create_user,name="createaccount"),#calls create_user function of views.py
    path('',views.homecreo,name="homecreo"),#calls homecreo function of views.py
    path('photos/',views.allimage,name="allimage"),#calls allimage function of views.py
    path('videos/',views.allvideo,name="allvideo"),#calls allvideo function of views.py
    path('audios/',views.allaudio,name="allaudio"),#calls allaudio function of views.py
    path('delete/<int:pk>',views.UserDeleteView.as_view(),name="deleteconfirm"),#calls UserDeleteView Delete class View of views.py
    path('userupdate/<int:pk>',views.UserUpdateView.as_view(),name="updateprofile"),#calls UserUpdateView Update class View of views.py
    path('portfolioupdate/<int:pk>',views.UserProfileUpdateView.as_view(),name="updateportfolio"),#calls UserProfileUpdateView  Update class vier function of views.py
    path('editprofile/',views.UpdateProfile,name="updateprofile"),#calls UpdateProfile function of views.py
    path('post/',views.PostFormView.as_view(),name="post"),#calls PostFormView create class view of views.py
    path('posts/<int:id>/',views.detailpost,name="detailpost"),#calls detailpost function of views.py
    path('<int:id>/comment/',views.addcomment,name="addcomment"),#calls addcomment function of views.py
    path('<int:id>/likes/',views.addlike,name="addlike"),#calls addlike function of views.py
    path('portfolio/<str:publisher>/',views.artistdetail,name="artistdetail"),#calls artistdetail function of views.py



]
