# django-creo
creo  https://creoverse.herokuapp.com/
    
    image,video and art sharing platform
    * *Like The Posts to Know about the Artist*


not completed 

# See Directory Tree Structure
```bash
.
├── Artist
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   │   ├── Artist
│   │   │   └── userprofileinfo_form.html
│   │   ├── artistdetail.html
│   │   ├── auth
│   │   │   ├── change_password.html
│   │   │   ├── user_confirm_delete.html
│   │   │   └── user_form.html
│   │   ├── createaccount.html
│   │   ├── profile.html
│   │   ├── savedpost.html
│   │   ├── testurl.html
│   │   └── updateprofile.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Creo
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── media
│   ├── image
│   │   └── icon
│   │       ├── creohome.jpg
│   │       ├── Ctitle.png
│   │       ├── github_logo2.png
│   │       ├── github_logo3.png
│   │       ├── github_logo.png
│   │       ├── like.png
│   │       └── title.png
│   ├── posts
│   │   └── cristiano_ronaldo_in_wpap__anomali__by_aylmerstreet-d9f8hyt.jpg
│   └── profilepics
│       ├── 42475510_1890629497649302_7255337937867374592_o.jpg
│       ├── default1.jpg
│       └── UTSAVFINAL.jpg
├── Posts
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   │   ├── allaudio.html
│   │   ├── allimage.html
│   │   ├── allindex.html
│   │   ├── allvideo.html
│   │   ├── detail.html
│   │   ├── Posts
│   │   │   ├── postsubmission_confirm_delete.html
│   │   │   └── postsubmission_form.html
│   │   ├── profile.html
│   │   ├── testurl.html
│   │   ├── updateprofile.html
│   │   └── user.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── requirements.txt
├── static
│   └── css
│       ├── intro.css
│       ├── logsign.css
│       ├── main.css
│       └── sample1.css
└── templates
    ├── base.html
    ├── footer.html
    ├── home.html
    ├── index.html
    └── signin.html

```
# How To Run
```bash
- Install Python and Pip
- Create A Virtual Environment 

Activate Virtual Environment

$ pip install -r requirements.txt

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver

```

