"""all the work and function is carried  out based on the request (mapped by urls.py)"""
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
#importing models from models.py
from creo.models import UserProfileInfo,PostSubmission,CommentPost,Likes
from django.contrib import messages
#importing from  forms.py
from creo.forms import UserForm,UserProfileInfoForm,CommentPostForm,LikePostButton,PostSubmissionForm,UserProfileInfoUpdateForm
#importing class views
from django.views.generic import DeleteView,CreateView,UpdateView
from django.contrib.auth.models import User
from django import forms
#for login and logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django import forms

# Create your views here.
def testurl(request,slug = 'mostviewed'):
    if slug=='mostviewed':    
        latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    elif slug=='mostliked':
        latest_submissions = PostSubmission.objects.order_by('-like_count','-view_count','-pub_date')
    elif slug=='newest':
        latest_submissions = PostSubmission.objects.order_by('-pub_date','-like_count','-view_count')
    else:
        latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')

    # template = loader.get_template('images/index.html')
    context = { 'latest_submissions': latest_submissions }
    return render(request, 'testurl.html', context)

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

def all_user(request):
    alluser = {"user_list":UserProfileInfo.objects.all}
    if not alluser:
        return render(request,"user.html")
    else:
        return render(request,"user.html",context=alluser)

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

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("index")
    #logout(request)
class UserUpdateView(UpdateView):
    fields = ('email',)
    model = User
    success_url = reverse_lazy("profile")
class UserProfileUpdateView(UpdateView):
    #fields = ('portfolio_site','profile_pic','bio','resume','gender')
    model = UserProfileInfo
    form_class = UserProfileInfoUpdateForm
    success_url = reverse_lazy("profile")
class PostFormView(CreateView):
    model = PostSubmission
    success_url = reverse_lazy("index")
    form_class = PostSubmissionForm 
    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

@login_required
def UpdateProfile(request):
    if request.user.is_authenticated:
        u = request.user
        alluser = {"alluser":UserProfileInfo.objects.get(user=request.user),'u':u}
        return render(request,"updateprofile.html",context=alluser)
    else:
        return HttpResponse("Please Login")

def homecreo(request):
    latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    # template = loader.get_template('images/index.html')
    context = { 'latest_submissions': latest_submissions }
    return render(request, 'allindex.html', context)

def allvideo(request):
    latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    # template = loader.get_template('images/index.html')
    context = { 'latest_submissions': latest_submissions }
    return render(request, 'allvideo.html', context)

def allimage(request):
    latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    # template = loader.get_template('images/index.html')
    context = { 'latest_submissions': latest_submissions }
    return render(request, 'allimage.html', context)
    
def allaudio(request):
    latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    # template = loader.get_template('images/index.html')
    context = { 'latest_submissions': latest_submissions }
    return render(request, 'allaudio.html', context)

def detailpost(request,id):
    submission = get_object_or_404(PostSubmission,pk=id)
    submission.view_count = F('view_count')+1
    submission.save()
    comments  = CommentPost.objects.filter(title_id  = submission.id)
    if request.user.is_authenticated:
        if Likes.objects.filter(post = submission,publisher=request.user).exists():
            liked = Likes.objects.get(post = submission,publisher=request.user)
            form = CommentPostForm()
            return render(request, 'detail.html', {'submission': submission,'comments':comments, 'form': form,'liked':liked})
        else:
            form = CommentPostForm()
            return render(request, 'detail.html', {'submission': submission,'comments':comments, 'form': form})
    #return render(request, 'detail.html', {'submission': submission,})#, 'form': form})
    else:
        form = CommentPostForm()
        return render(request, 'detail.html', {'submission': submission,'comments':comments, 'form': form})
    #return render(request, 'detail.html', {'submission': submission,})#, 'form': form})

def artistdetail(request,publisher):
    artistinfo = get_object_or_404(User,username=publisher)
    artistinfo2 = get_object_or_404(UserProfileInfo,user_id=artistinfo.id)
    artistposts = PostSubmission.objects.filter(publisher_id=artistinfo.id)
    #form = CommentForm()
    return render(request, 'artistdetail.html', {'artistinfo': artistinfo,'artistinfo2': artistinfo2,'artistposts':artistposts})#, 'form': form})

def addcomment(request,id):
    current_submission = get_object_or_404(PostSubmission,pk=id)
    if request.user.is_authenticated:
        if request.method =="POST":
            comment_form = CommentPostForm(request.POST)
            if comment_form.is_valid():
                comment = CommentPost(title=current_submission, comment=comment_form.cleaned_data['comment'],publisher=request.user)
                comment.save()
                current_submission.comment_count = F('comment_count')+1
                current_submission.save()
            return HttpResponseRedirect(reverse('detailpost', args=(id,)))
        else:
            return(detailpost(request,id))
    else:
        return(signin(request))

def addlike(request,id):
    current_submission = get_object_or_404(PostSubmission,pk=id)
    if request.user.is_authenticated:
        if request.method =="POST":
            if Likes.objects.filter(post = current_submission,publisher=request.user).exists():
                liked = Likes.objects.get(post = current_submission,publisher=request.user)
                if liked.like == True:
                    liked.like = False
                    liked.save()
                    current_submission.like_count = F('like_count')-1
                    current_submission.save()
                else :
                    liked.like = True
                    liked.save()
                    current_submission.like_count = F('like_count')+1
                    current_submission.save()
            else:
                like = Likes(post=current_submission,like=True,publisher=request.user)
                like.save()
                current_submission.like_count = F('like_count')+1
                current_submission.save()
            return HttpResponseRedirect(reverse('detailpost', args=(id,)))
        else:
            return(detailpost(request,id))
    else:
        return(signin(request))

"""def myposts(request):
    posts = PostSubmission.objects.get(publisher=request.user)"""