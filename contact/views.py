from django.shortcuts import render
from django.http.response import JsonResponse
from .models import contact_form_details
# Create your views here.

def add_contact_form_detail_db(request):
    print('---------------------------------> get request dictionary data ', request.POST.keys())
    name_form_field_data = request.POST['name']
    contact_form_field_data = int(request.POST['contact'])
    email_form_field_data = request.POST['email']
    message_form_field_data = request.POST['message']
    print("-----------------------------------------------------------> ", name_form_field_data, email_form_field_data, message_form_field_data)
    response_data = {}
    try:
        contact_form_details_obj = contact_form_details(name=name_form_field_data,contact=contact_form_field_data, email=email_form_field_data, message=message_form_field_data)
        contact_form_details_obj.save()
        response_data = {'valid':True}
    except Exception as e :
        print('-------------------------------->error', e)
        response_data = {'valid':False}
    return JsonResponse(response_data, safe=False)