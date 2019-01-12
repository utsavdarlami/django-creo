# django-creo
creo  https://creoverse.herokuapp.com/
    
    image,video and art sharing platform
    * *Like The Posts to Know about the Artist*


not completed 

# See Directory Tree Structure
```bash
.
├── _config.yml
├── creo
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   ├── allaudio.html
│   │   ├── allimage.html
│   │   ├── allindex.html
│   │   ├── allvideo.html
│   │   ├── artistdetail.html
│   │   ├── auth
│   │   │   ├── user_confirm_delete.html
│   │   │   └── user_form.html
│   │   ├── createaccount.html
│   │   ├── creo
│   │   │   ├── postsubmission_form.html
│   │   │   └── userprofileinfo_form.html
│   │   ├── detail.html
│   │   ├── profile.html
│   │   ├── updateprofile.html
│   │   └── user.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── creo.pdf
├── db.sqlite3
├── manage.py
├── media
│   ├── postedpics
│   │   ├── gcwqq1of8vm01.jpg
│   │   ├── grub_0.jpg
│   │   ├── homejpg.jpg
│   │   ├── ohzmiiuecq621.jpg
│   │   ├── Screenshot_from_2018-09-22_20-14-27_91bixcf.png
│   │   ├── Screenshot_from_2018-09-22_20-14-27.png
│   │   ├── Screenshot_from_2018-09-22_20-14-27_QQG9uow.png
│   │   ├── ss.jpg
│   │   └── thanos-funny-artwork-xd-1024x768.jpg
│   ├── posts
│   │   ├── Pink_Floyd_-_Wish_You_Were_Here.mp3
│   │   └── test1.mp4
│   ├── profilepics
│   │   ├── batmanlogo.jpg
│   │   ├── default1.jpg
│   │   ├── default.png
│   │   ├── DSC01794_7DgXxZJ.jpg
│   │   ├── DSC01794.jpg
│   │   ├── elon_agz1HhN.jpg
│   │   ├── elon.jpg
│   │   ├── elon_nPnSUD4.jpg
│   │   ├── freaksgeeks.jpg
│   │   ├── img5.jpg
│   │   ├── neo.png
│   │   ├── stormtrooper.jpg
│   │   └── venom-2018-movie-poster-f9-1024x768.jpg
│   └── resumes
│       └── creo.pdf
├── README.md
├── requirements.txt
├── secondproject
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── css
│   │   ├── intro.css
│   │   ├── logsign.css
│   │   └── main.css
│   └── image
│       └── icon
│           ├── like.png
│           └── title.png
└── templates
    ├── base.html
    ├── home.html
    ├── index.html
    └── signin.html
```
# How To Run
```bash
-Install Python and Pip
- Create A Virtual Environment 
Inside Virtual Environment
$ pip install -r requirements.txt
--> remove STATIC_ROOT in line (127 and 130) and STATICFILES_STORAGE in line 125 from settings.py
$ python manage.py runserver

```

