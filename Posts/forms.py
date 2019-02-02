from django import forms
from django.contrib.auth.models import User
from Posts.models import CommentPost,PostSubmission


class CommentPostForm(forms.ModelForm):
    comment= forms.CharField(label='',max_length=500,
                            widget=forms.Textarea(
                            attrs = {"class"     :"form-control col-15",
                                    'rows'       :3,
                                    'cols'       :22,
                                    'style'      :'resize:none;',}
                                )
                        )
    class Meta():
        model = CommentPost
        fields = ('comment',)
        exclude = ('title','publisher','pub_date',)


class PostSubmissionForm(forms.ModelForm):
    POST_CHOICES = ((0, 'Image'),(1, 'Video'),(2,'Audio'))   
    title = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control is-valid", "id":"exampleInputUserName1","placeholder":"Enter Title"}))
    post_type = forms.ChoiceField(choices=POST_CHOICES,label = "Choice The Type Of Content You Are Posting", widget=forms.RadioSelect(attrs={"type":"radio","id":"customRadio1","class":"custom-control-input"}),)
    class Meta():
        model = PostSubmission
        fields=('title','description','content','post_type')
        exclude=('pub_date','publisher','pub_date',)