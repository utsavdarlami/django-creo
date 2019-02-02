"""all the work and function is carried  out based on the request (mapped by urls.py)"""
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
#importing models from models.py
from Artist.models import UserProfileInfo,SavedPost
from Posts.models import PostSubmission,CommentPost,Likes
from django.contrib import messages
#importing from  forms.py
from Artist.forms import UserForm,UserProfileInfoForm,UserProfileInfoUpdateForm
from Posts.forms import CommentPostForm,PostSubmissionForm
#importing class views
from django.views.generic import DeleteView,CreateView,UpdateView
from django.contrib.auth.models import User
from django import forms
#for login and logout
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse,reverse_lazy
from django import forms
# Create your views here.

def index(request):
    return render(request,"index.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return(HttpResponseRedirect(reverse('homecreo')))
            else:
                return(HttpResponse("ACCOUNT IS NOT ACTIVE"))
        else :
            messages.success(request,"Sorry ,that login was invalid. Please try again.")
            return(HttpResponseRedirect(reverse('signin')))

    else:
        return render(request,"signin.html")

@login_required
def user_logout(request):
    logout(request)
    return(HttpResponseRedirect(reverse('index')))

@login_required
def profile(request):
    if request.user.is_authenticated:
        u = request.user
        alluser = {"alluser":UserProfileInfo.objects.get(user=request.user),'u':u,"artistposts":PostSubmission.objects.filter(publisher=request.user)}
        return render(request,"profile.html",context=alluser)
    else:
        return HttpResponse("Please Login")

def create_user(request):
    registered  = False
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
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
    value = {"user_form":user_form,"profile_form":profile_form,"registered":registered}
    return render(request,"createaccount.html",context = value)

def change_password(request,pk):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('signin'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'cp_form': form}
        return render(request, 'auth/change_password.html', args)

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("index")
    #logout(request)
class UserUpdateView(UpdateView):
    fields = ('email','first_name','last_name')
    model = User
    success_url = reverse_lazy("profile")
    #  template_name = 'my-book-detail.html'
    
class UserProfileUpdateView(UpdateView):
    #fields = ('portfolio_site','profile_pic','bio','resume','gender')
    model = UserProfileInfo
    form_class = UserProfileInfoUpdateForm
    success_url = reverse_lazy("profile")

@login_required
def UpdateProfile(request):
    if request.user.is_authenticated:
        u = request.user
        alluser = {"alluser":UserProfileInfo.objects.get(user=request.user),'u':u}
        return render(request,"updateprofile.html",context=alluser)
    else:
        return HttpResponse("Please Login")

def artistdetail(request,publisher):
    artistinfo = get_object_or_404(User,username=publisher)
    artistinfo2 = get_object_or_404(UserProfileInfo,user_id=artistinfo.id)
    artistposts = PostSubmission.objects.filter(publisher_id=artistinfo.id)
    #form = CommentForm()
    return render(request, 'artistdetail.html', {'artistinfo': artistinfo,'artistinfo2': artistinfo2,'artistposts':artistposts})#, 'form': form})

def savethispost(request,id):
    current_submission = get_object_or_404(PostSubmission,pk=id)
    request.method="POST"
    if request.user.is_authenticated:
        if request.method =="POST":
            if SavedPost.objects.filter(post = current_submission,savedby=request.user).exists():
                saved = SavedPost.objects.get(post = current_submission,savedby=request.user)
                if saved.save_post == True:
                    saved.save_post = False
                    saved.save()
                else :
                    saved.save_post = True
                    saved.save()
            else:
                initial_save = SavedPost(post=current_submission,save_post=True,savedby=request.user)
                initial_save.save()
            return HttpResponseRedirect(reverse('detailpost', args=(id,)))
        else:
            return HttpResponseRedirect(reverse('detailpost', args=(id,)))
    else:
        return(signin(request))

def mysavedpost(request):
    all_save_posts=[]
    saved_posts_list  = SavedPost.objects.filter(savedby  = request.user,save_post=True)
    if saved_posts_list:
        for posts in saved_posts_list:
            saved_posts = PostSubmission.objects.filter(pk=posts.post_id)
            all_save_posts.append(saved_posts)
        return render(request, 'savedpost.html', {'saved_posts': all_save_posts,})
    else :
        return render(request, 'savedpost.html',)
