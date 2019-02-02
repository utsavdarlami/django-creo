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

def homecreo(request,slug=None):
    if slug=='mostviewed':    
        latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    elif slug=='mostliked':
        latest_submissions = PostSubmission.objects.order_by('-like_count','-pub_date','-view_count')
    elif slug=='newest':
        latest_submissions = PostSubmission.objects.order_by('-pub_date','-like_count','-view_count')
    else:
        latest_submissions = PostSubmission.objects.order_by('-view_count','-pub_date','-like_count')

    context = { 'latest_submissions': latest_submissions }
    return render(request, 'allindex.html', context)

class PostFormView(CreateView):
    model = PostSubmission
    success_url = reverse_lazy("index")
    form_class = PostSubmissionForm 
    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model= PostSubmission
    fields=('title','description',)
    success_url = reverse_lazy("profile")
    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = PostSubmission
    success_url = reverse_lazy("profile")

def allvideo(request,slug=None):
    if slug=='mostviewed':    
        latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    elif slug=='mostliked':
        latest_submissions = PostSubmission.objects.order_by('-like_count','-pub_date','-view_count')
    elif slug=='newest':
        latest_submissions = PostSubmission.objects.order_by('-pub_date','-like_count','-view_count')
    else:
        latest_submissions = PostSubmission.objects.order_by('-view_count','-pub_date','-like_count')

    context = { 'latest_submissions': latest_submissions }    # template = loader.get_template('images/index.html')
    return render(request, 'allvideo.html', context)

def allimage(request,slug=None):
    if slug=='mostviewed':    
        latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    elif slug=='mostliked':
        latest_submissions = PostSubmission.objects.order_by('-like_count','-pub_date','-view_count')
    elif slug=='newest':
        latest_submissions = PostSubmission.objects.order_by('-pub_date','-like_count','-view_count')
    else:
        latest_submissions = PostSubmission.objects.order_by('-view_count','-pub_date','-like_count')

    context = { 'latest_submissions': latest_submissions }
    return render(request, 'allimage.html', context)
    
def allaudio(request,slug=None):
    if slug=='mostviewed':    
        latest_submissions = PostSubmission.objects.order_by('-view_count','-like_count','-pub_date')
    elif slug=='mostliked':
        latest_submissions = PostSubmission.objects.order_by('-like_count','-pub_date','-view_count')
    elif slug=='newest':
        latest_submissions = PostSubmission.objects.order_by('-pub_date','-like_count','-view_count')
    else:
        latest_submissions = PostSubmission.objects.order_by('-view_count','-pub_date','-like_count')

    context = { 'latest_submissions': latest_submissions }
    return render(request, 'allaudio.html', context)

def detailpost(request,id):
    submission = get_object_or_404(PostSubmission,pk=id)
    submission.view_count = F('view_count')+1
    submission.save()
    comments  = CommentPost.objects.filter(title_id  = submission.id)
    if request.user.is_authenticated:
        if SavedPost.objects.filter(post = submission,savedby=request.user).exists():
            saved = SavedPost.objects.get(post = submission,savedby=request.user)
        else:
            saved = None
        if Likes.objects.filter(post = submission,publisher=request.user).exists():
            liked = Likes.objects.get(post = submission,publisher=request.user)
            form = CommentPostForm()
            return render(request, 'detail.html', {'submission': submission,'comments':comments, 'form': form,'liked':liked,'saved':saved})
        else:
            form = CommentPostForm()
            return render(request, 'detail.html', {'submission': submission,'comments':comments, 'form': form,'saved':saved})
    #return render(request, 'detail.html', {'submission': submission,})#, 'form': form})
    else:
        form = CommentPostForm()
        return render(request, 'detail.html', {'submission': submission,'comments':comments, 'form': form})
    #return render(request, 'detail.html', {'submission': submission,})#, 'form': form})

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
        return render(request,"signin.html")

def addlike(request,id):
    current_submission = get_object_or_404(PostSubmission,pk=id)
    request.method="POST"
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
                    #notify.send(User.objects.get(username=request.user).username, recipient=current_submission.id, verb='Liked Your Post')
            else:
                like = Likes(post=current_submission,like=True,publisher=request.user)
                like.save()
                current_submission.like_count = F('like_count')+1
                current_submission.save()
            return HttpResponseRedirect(reverse('detailpost', args=(id,)))
        else:
            return(detailpost(request,id))
    else:
        return render(request,"signin.html")

