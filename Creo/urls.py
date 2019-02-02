"""Creo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#url request which is mapped to  functions of views.py( inside creo folder)

from django.contrib import admin
from django.urls import path
#import views from Artist as ar
#import views from Posts as pv
#from Artist import views as artistviews #importing views.py in  Artist folder
import Posts.views as pv # importing views.py in Posts Folder
import Artist.views as av # importing views.py in Artist Folder

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pv.homecreo,name="index"),#calls homecreo function of views.py
    path('signin/',av.signin,name="signin"),#calls singin  function of views.py 
    path('artist/',include('Artist.urls')),#url for app =creo
    path('posts/',include('Posts.urls')),#url for app =creo
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
