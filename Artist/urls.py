from django.urls import path
from . import views
#url request which is mapped to  functions of views.py( inside creo folder)
urlpatterns = [
  # 11 urls
  path('profile/',views.profile,name="profile"),#calls profile function of views.py
  path('signout/',views.user_logout,name="user_logout"),#calls user_logout function of views.py
  path('createaccount/',views.create_user,name="createaccount"),#calls create_user function of views.py
  # User Account
  path('delete/<int:pk>',views.UserDeleteView.as_view(),name="deleteconfirm"),#calls UserDeleteView Delete class View of views.py
  path('userupdate/<int:pk>',views.UserUpdateView.as_view(),name="updateprofile"),#calls UserUpdateView Update class View of views.py
  path('portfolioupdate/<int:pk>',views.UserProfileUpdateView.as_view(),name="updateportfolio"),#calls UserProfileUpdateView  Update class vier function of views.py
  path('editprofile/',views.UpdateProfile,name="updateprofile"),#calls UpdateProfile function of views.py
  path('changepassword/<int:pk>',views.change_password,name="changepassword"),
  #path('changepassword/<int:pk>',views.UserPasswordChangeView.as_view(),name="changepassword"),#calls UserProfileUpdateView  Update class vier function of views.py
  #portfolio view
  path('portfolio/<str:publisher>/',views.artistdetail,name="artistdetail"),#calls artistdetail function of views.py
  #path('mysaves/',views.mysaves,name="mysaves"),
  path('<int:id>/saved/',views.savethispost,name="saved"),
  path('mysaves/',views.mysavedpost,name="mysaves"),
]
