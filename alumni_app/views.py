from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from alumni_app import forms
from alumni_app.forms import signupform,userform,signupform_update,userform_update,postform,commentsform,eventform,aids,tracker_form
from alumni_app.models import user_signup,notice,post,comment,event,track,upcoming_event
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import logout




a=0
def index(request):
    description=notice.objects.all()
    upcomming=upcoming_event.objects.all()
    return render(request,'alumni_app/home.html',{
                             'description':description,
                             'upcomming':upcomming,
                             })

# def signup(request):
#     return render(request,'alumni_app/signup.html',)

# Create your views here.

def signup(request):

    registred=False

    if request.method =="POST":
        user_form=userform(data=request.POST)
        signup_form=signupform(data=request.POST)

        if user_form.is_valid() and signup_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile=signup_form.save(commit=False)
            profile.user=user

            if 'image' in request.FILES:
                profile.image=request.FILES['image']            
            
            profile.save()

            registred=True


        else:
            print(user_form.errors,signup_form.errors)
    else:
        user_form=userform()
        signup_form=signupform()

    return render(request,'alumni_app/signup.html',
                            {'user_form':user_form,
                             'signup_form':signup_form,
                             'registred':registred,}
                                )


def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                # print("Login successful")
                messages.success(request, "Logged in Successfully!")
                return render(request,'alumni_app/profile.html')


            else:
                return HttpResponse("Acount not Active")
        else:
            print("Anauthorised Entry")
            return HttpResponse("Invalid login request")
    else:
        return render(request,'alumni_app/signin.html')


def logout_view(request):
    logout(request)




def profile(request):
    return render(request,'alumni_app/profile.html',
                            {'user_form':user_form,
                             'signup_form':signup_form,
                             'registred':registred,
                            }
                                )



def about_page(request):
    return render(request,'alumni_app/about_page.html')


def edit_profile(request):
    registred=False

    if request.method =="POST":

        user_form=userform_update(request.POST,instance=request.user)
        signup_form=signupform_update(request.POST,request.FILES,instance=request.user.user_signup)

        if user_form.is_valid() and signup_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile=signup_form.save(commit=False)
            profile.user=user

            if 'image' in request.FILES:
                profile.image=request.FILES['image']            
            
                profile.save()

                registred=True


        else:
           print(user_form.errors,signup_form.errors)
    else:
        user_form=userform()
        signup_form=signupform()
    return render(request,'alumni_app/edit_profile.html',
                            {'user_form':user_form,
                             'signup_form':signup_form,
                             'registred':registred,}
                                )


def contact(request):
    return render(request,'alumni_app/contact.html')




def forum(request):
    registred=False

    if request.method =="POST":
        post_form=postform(data=request.POST)


        if post_form.is_valid():
            post=post_form.save()
            registred=True
    
    return render(request,'alumni_app/forum.html',
                            {'post_form':postform,
                            'registred':registred,}
                            )



# def comments(request):
#     registred=False

#     if request.method =="POST":
#         comment_form=commentsform(data=request.POST)

#         if comment_form.is_valid():
#             comment=comment_form.save()
#             registred=True

#     return render(request,'alumni_app/post.html',
#                             {'comment_form':commentsform,
#                             'registred':registred,}
#                             )

def forumView(request):
    post_all=post.objects.all().order_by('-post_no')
    return render(request,'alumni_app/forum_view.html',{
                             'post':post_all,'a':a,
                             })


def comment_page(request):

    comments=comment.objects.all()
    trackit=track.objects.all()[:1].get()
    add=trackit.tarcker
    tracked=comments.all().filter(comment_no=add)


    registred=False

    if request.method =="POST":
        comment_form=commentsform(data=request.POST)

        if comment_form.is_valid():
            mycomment=comment_form.save()
            registred=True



    return render(request,'alumni_app/post_comment.html',{
                                'comment':comments, 'tracked':tracked,
                                'comment_form':commentsform,
                                'registred':registred,
                                'one':1,
                                
                            })



def council_page(request):
    member=user_signup.objects.all()
    return render(request,'alumni_app/council.html',{
                             'member':member,
                             })


def event_page(request):
    event_all=event.objects.all()
    return render(request,'alumni_app/event_page.html',{
        'event':event_all,
    })


def aiding(request):      #this one is for getting post id of any post and then redirect to addetailspage
    a=1
    if request.method=="POST":
        a=int(request.POST.get('id'))
        t=track.objects.all()[:1].get()
        t.tarcker=a
        t.save()
        return redirect('signin/forum_view/comment')
    else:
        return render(request,'alumni_app/forum_view.html')