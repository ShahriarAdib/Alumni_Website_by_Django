from django import forms
from django.contrib.auth.models import User
from alumni_app.models import user_signup
from alumni_app.models import notice,post,comment,event,track,upcoming_event



class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')


class signupform(forms.ModelForm):
    class Meta():
        model=user_signup
        fields=('Name','Mobile','Address','Series','image')


class notice(forms.ModelForm):
    class Meta():
        model=notice
        fields=('notice_no','description',)


class userform_update(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')


class signupform_update(forms.ModelForm):
    class Meta():
        model=user_signup
        fields=('Name','Mobile','Address','Series','image')


        
class postform(forms.ModelForm):
    class Meta():
        model=post
        fields=('author','title','text',)


class commentsform(forms.ModelForm):
    class Meta():
        model=comment
        fields=('comment_no','author','text',)


class eventform(forms.ModelForm):
    class Meta():
        model=event
        fields=('event_title','event_description','event_picture')



class tracker_form(forms.ModelForm):
    class Meta():
        model=track
        fields=('tarcker',)

class aids(forms.Form):
    ids=forms.IntegerField()


