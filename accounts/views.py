# from django.shortcuts import render
from posixpath import split
from sre_constants import SUCCESS
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import random
# Create your views here.
def login(request):
    return JsonResponse({'msg':'SUCCESS'})

def add_account(request):
    if request.method == 'POST':
        email = request.POST.get('email',None)
        pwd = str(random.random()*1000000).split['.'][0]
        User.objects.create_user(email.split('@')[0], email, pwd)
        # send mail

def set_pwd(request):
    if request.method == 'POST':
        pwd = request.POST.get('pwd', None)
        if pwd != None:
            u = User.objects.get(username='john')
            u.set_password('new password')
            u.save()
        else:
            pass
    return JsonResponse()



# user = authenticate(username='john', password='secret')
# if user is not None:
#     # A backend authenticated the credentials
# else:
#     # No backend authenticated the credentials


