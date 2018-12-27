from django.urls import path
from . import views
urlpatterns = [
    path('users/',views.all_user,name="allusers"),
    path('profile/',views.profile,name="profile"),
    path('signout/',views.user_logout,name="user_logout"),
    path('createaccount/',views.create_user,name="createaccount"),
    path('',views.homecreo,name="homecreo"),
    path('delete/<int:pk>',views.UserDeleteView.as_view(),name="deleteconfirm"),
    path('post/',views.PostFormView.as_view(),name="post"),
    path('photos/<int:id>/',views.detailpost,name="detailpost"),
    path('<int:id>/comment/',views.addcomment,name="addcomment"),
    path('portfolio/<str:publisher>/',views.artistdetail,name="artistdetail"),



]
