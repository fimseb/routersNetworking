from datetime import date
from django.http import JsonResponse
from django.shortcuts import render
from routersNetworkHtmlPages.models import State, District, Testimonial, News, DOT, Hardware
from .models import DOT, Query, Subscribe
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    testimonial_obj = Testimonial.objects.all()
    path = 'media/'
    return render(request, 'routersNetworkHtmlPages/index.html', context={'testimonial_obj': testimonial_obj, 'path':path})


def about(request):
    return render(request, 'routersNetworkHtmlPages/about.html')

@csrf_exempt
def subscribe(request):
    if request.POST.get('useremail', None) != None:
        email = request.POST['useremail']
        try:
            obj = Subscribe.objects.get(user_email=email)
        except:
            obj = Subscribe(user_email=email)
            obj.save()
    print('--------------> call come here')
    return JsonResponse({'valid':'True'})

def ISP(request):
    return render(request, 'routersNetworkHtmlPages/ISPservice.html')


def telco(request):
    return render(request, 'routersNetworkHtmlPages/TelcoResource.html')


def technical(request):
    return render(request, 'routersNetworkHtmlPages/TechnicalConsultancy.html')


def news(request):
    news = News.objects.all().order_by('-date','-time')[:25]
    dots = DOT.objects.all().order_by('-date','-time')[:25]
    for i in news:
        print(i)
    for i in dots:
        print(i)
    hardware_list = Hardware.objects.all().order_by('-created_date')[:20]
    return render(request, 'routersNetworkHtmlPages/news.html', context={'news': news, 'dots': dots, 'path' : 'media/', 'hardware_list_obj': hardware_list})


def contact(request):
    states = State.objects.all()
    for s in states:
        print(s.state_id, s.state)
    return render(request, 'routersNetworkHtmlPages/contact.html', context= {'state_obj':states})
    

def hardware_detail(request,id):
    obj = Hardware.objects.get(hardware_id=id)
    print(obj)
    return render(request, 'routersNetworkHtmlPages/detail.html', context={'path':'media/','obj':obj})

def district(request):
    state_id = request.GET['state']
    district_obj = District.objects.filter(state_id=state_id)
    res = {}
    # print('--------------------------------> district object', district_obj)
    for i in district_obj :
        res[str(i.district_id)] = i.name
    # print('---------------------------------->res', res)
    return JsonResponse({'district_obj':res})
   
@csrf_exempt
def contact_form_data(request):
    print('----------------------->', request.POST.keys())
    name = request.POST['name']
    company = request.POST['company']
    state = request.POST['state']
    district = request.POST['district']
    pincode = request.POST['pincode']
    contact = request.POST['contact']
    address = request.POST['address']
    license = request.POST['license']
    query = request.POST['query']
    state_obj = State.objects.get(state_id=state)
    print('---------------> state obj', state_obj)
    # print('------------------------------->api result:', name, company, state, district, pincode, contact, address, license, query)
    try:
        # raise NameError('HiThere')
        if request.POST.keys() != None:
            q = Query(
                name = name,
                company_name = company,
                state = state_obj,
                district = district,
                pincode = pincode,
                contact = contact,
                address = address,
                license = license,
                query_msg = query,
            )
            
            q.save()
            # print('-----------------> Data', request.POST.keys())
            return JsonResponse({'valid':'True'})
    except Exception:
        print('-------------------->    run')
        return JsonResponse({'valid':''})
    return JsonResponse({'valid':''})

