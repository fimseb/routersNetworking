# from distutils.command.upload import upload
# import imp
# from inspect import signature
# from statistics import mode
# from unicodedata import name
from datetime import datetime
from http import client
from pyexpat import model
from statistics import mode
from tkinter.tix import Tree
from turtle import title
from unicodedata import category
from django.db import models
# from datetime import date, time
from django.contrib.auth.models import User


# Create your models here.

class Query(models.Model) :
    query_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    company_name = models.CharField(max_length=512)
    state  = models.CharField(max_length=64)
    district = models.CharField(max_length=512)
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=512)
    license = models.CharField(max_length=100)
    query_msg = models.TextField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    query_assign_to_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='task_given')
    query_assign_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='task_assign')

    def __str__(self) -> str:
        return self.company_name


class Testimonial(models.Model) :
    testimonial_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='testimonial')
    review_text = models.TextField()
    signature = models.CharField(max_length=128)
    designation = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=64, null=False)

    def __str__(self) -> str:
        return self.state

class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=64)
    news_discription = models.TextField()
    pdf = models.FileField(upload_to='news')
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.news_title


class DOT(models.Model):
    news_id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=64)
    news_discription = models.TextField()
    pdf = models.FileField(upload_to='dots')
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.news_title


class Subscribe(models.Model):
    user_email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.user_email

import datetime

def getfilename(filename):
    name_lis = filename.split('.')
    return name_lis[0]+str(datetime.datetime.now())+name_lis[-1]

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.id, filename)
    return 'hardware/{0}'.format(getfilename(filename))

class Hardware(models.Model):
    hardware_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    discription_title = models.CharField(max_length=64, default=None, blank=True, null=True)
    discription = models.TextField()
    category = models.CharField(max_length=256)
    hardware_client = models.CharField(max_length=256, verbose_name='Procduct\'s Company')
    url = models.URLField(max_length=500, default=None, blank=True)
    created_date = models.DateField(auto_now_add=True)
    # is_photo = models.BooleanField(default=False, verbose_name='Have Product Other Images')
    photo = models.FileField(upload_to=user_directory_path, verbose_name='Hardware Photo', blank=True, null=True, default=True)
    visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class hardware_photo(models.Model):
    hardware_photo_id = models.AutoField(primary_key=True)
    hardware_id = models.ForeignKey(Hardware,on_delete=models.CASCADE)
    images = models.FileField(upload_to='media/hardware/',verbose_name='Product Photo')
    created_datetime = models.DateTimeField(auto_created=True)