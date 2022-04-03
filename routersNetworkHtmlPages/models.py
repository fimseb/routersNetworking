# from distutils.command.upload import upload
# import imp
# from inspect import signature
# from statistics import mode
# from unicodedata import name
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

