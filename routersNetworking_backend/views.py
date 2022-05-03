
from django.db.models import Q
# from django.shortcuts import render
from django.http import JsonResponse
from routersNetworkHtmlPages.models import State, District,Query
from functools import reduce
import operator
# import json

# Create your views here.
def add_state_api(request):
    state_data = request.POST['state']
    # state_data = state_data.capitalize()
    print('--------------------> state data', state_data)
    try:
        state_obj = State.objects.get(state=state_data)        
    except Exception as e:
        print('-------------------> exception', e)
        State.objects.create(state=state_data)
        return JsonResponse({'msg':'State Added Successfully!!!'})
    print('----------------------------------> obj', state_obj)
    if  state_obj.state == state_data:
        return JsonResponse({'msg':'State is Already Exist!!!'})
    

def add_district_api(request):
    state_data = request.POST['state']
    district_data = request.POST['district']
    state_data = state_data.capitalize()
    district_data = district_data.capitalize()
    state_obj = None
    # print('------------------------------------------>',type(state_data),type(district_data)) 
    try:
        dis_obj = District.objects.filter(state_id__state=state_data, name=district_data)
        if len(dis_obj) == 0 :
            raise Exception("District Not Found")
# Exception("Sorry, no numbers below zero")

        return JsonResponse({'msg':'District is Already Exist!!!'}, safe=False)
    except Exception as e:
        # print('------------------------------> create 1', e,type(state_data))
        try:
            state_obj = State.objects.get(state=state_data)
            print('-----------------> inside state try')
        except Exception as e:
            # print('-----------------> 2', e)
            return JsonResponse('State Doest Not Exist. Please Add State!!!', safe=False)
        # print('------------------------------> create 2 ')
        District.objects.create(state_id=state_obj, name=district_data)
        return JsonResponse({'msg':'District Added Successfully!!!'}, safe=False)
    # except Exception as e:
    #     print('------------------->', e)
    #     return JsonResponse({'msg':'Internal Server Error Please Try Again!!!'})



def get_query_filter_result(request):
    my_filter = {}
    for form_data_key,form_data_values in request.POST.items():
        my_filter[str(form_data_key)] = str(form_data_values)
    filter_query_res = Query.objects.filter(reduce(operator.and_, (Q(**d) for d in [dict([i]) for i in my_filter.items()])))
    return JsonResponse({'query_res':filter_query_res})

def add_testimonial(request):

    return JsonResponse()

def add_market_trend(request):
    
    return JsonResponse()

def add_dot(request):
    
    return JsonResponse()

def add_hardware(request):
    
    return JsonResponse()

def get_hardware_list(request):

    return JsonResponse()

def get_hardware_detail(request,hardware_id):

    return JsonResponse()

def edit_hardware_display_list(request,hardware_id):

    return JsonResponse()

def send_mail_to_all_subscriber():
    
    return JsonResponse()