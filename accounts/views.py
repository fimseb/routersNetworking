# from django.shortcuts import render
from sre_constants import SUCCESS
from django.http import JsonResponse

# Create your views here.
def login(request):
    return JsonResponse({'msg':'SUCCESS'})
