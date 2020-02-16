from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.

class user_signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=264)
    Mobile=models.CharField(max_length=11)
    Address=models.CharField(max_length=264)
    Series=models.CharField(max_length=264)
    image=models.ImageField(blank='True')


    def __str__(self):
        return self.user.username


class notice(models.Model):
    notice_no= models.AutoField(primary_key=True)
    description=models.CharField(max_length=500)
    notice_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.notice_no)



class post(models.Model):
    post_no= models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post_no)


class comment(models.Model):
    comment_no= models.ForeignKey(post,'post_no')
    author = models.CharField(max_length=100)
    text = models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment_no)


class event(models.Model):
    event_no = models.AutoField(primary_key=True)
    event_title =  models.CharField(max_length=200)
    event_description=  models.CharField(max_length=500)
    event_picture=  models.ImageField(blank='True')

    def __str__(self):
        return str(self.event_no)



class track(models.Model):
    tarcker=models.IntegerField(default=0)

    def __str__(self):
        return "hell"


class upcoming_event(models.Model):
    serial= models.AutoField(primary_key=True)
    event_title =  models.CharField(max_length=200)
    event_description=  models.CharField(max_length=500)
    event_picture=  models.ImageField(blank='True')

    def __str__(self):
        return str(self.serial)
