from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from creo.models import UserProfileInfo
from django.contrib import messages
from creo.forms import UserForm,UserProfileInfoForm
#for login and logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse 


# Create your views here.

def index(request):
    return render(request,"index.html")

@login_required
def home(request):
       return render(request,"home.html")

    
def signin(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return(HttpResponseRedirect(reverse('home')))
            else:
                return(HttpResponse("ACCOUNT IS NOT ACTIVE"))
        else : 
            return HttpResponse("InValid Login Details")
    else:
        return render(request,"signin.html")

@login_required
def user_logout(request):
    logout(request)
    return(HttpResponseRedirect(reverse('index')))

#@login_required
def profile(request):
    if request.user.is_authenticated:
        email = request.user.email
        alluser = {"alluser":UserProfileInfo.objects.get(user=request.user),'email':email}
        return render(request,"profile.html",context=alluser)
    else:
        return HttpResponse("Please Login")

def all_user(request):
    alluser = {"user_list":UserProfileInfo.objects.all}
    return render(request,"user.html",context=alluser)

def create_user(request):
    registered  = False
    #accountcreateform = forms.AccountCreateForm()
    if request.method =="POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if (user_form.is_valid() and profile_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return index(request)
        else:
            messages.error(request, "Error!")
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        value = {"user_form":user_form,"profile_form":profile_form,"registered":registered}
    return render(request,"createaccount.html",context = value)


