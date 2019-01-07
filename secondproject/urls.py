"""secondproject URL Configuration

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
from creo import views #importing views.py in  creo folder
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

app_name = "creo"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homecreo,name="index"),#calls homecreo function of views.py
    path('signin/',views.signin,name="signin"),#calls singin  function of views.py 
    
    path('creo/',include('creo.urls')),#url for app =creo
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
