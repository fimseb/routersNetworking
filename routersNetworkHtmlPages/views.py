from datetime import date
from django.http import JsonResponse
from django.shortcuts import render
from routersNetworkHtmlPages.models import State, District, Testimonial, News
from .models import Query
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    testimonial_obj = Testimonial.objects.all()
    path = 'media/'
    return render(request, 'routersNetworkHtmlPages/index.html', context={'testimonial_obj': testimonial_obj, 'path':path})


def about(request):
    return render(request, 'routersNetworkHtmlPages/about.html')


def test(request):
    return render(request,'AdminLTE-3.2.0\index.html')

def ISP(request):
    return render(request, 'routersNetworkHtmlPages/ISPservice.html')


def telco(request):
    return render(request, 'routersNetworkHtmlPages/TelcoResource.html')


def technical(request):
    return render(request, 'routersNetworkHtmlPages/TechnicalConsultancy.html')


def news(request):
    news = News.objects.all().order_by('-date','-time')
    for i in news:
        print(i)
    return render(request, 'routersNetworkHtmlPages/news.html', context={'news': news, 'path' : 'media/'})


def contact(request):
    states = State.objects.all()
    for s in states:
        print(s.state_id, s.state)
    return render(request, 'routersNetworkHtmlPages/contact.html', context= {'state_obj':states})
    

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
    # print('------------------------------->api result:', name, company, state, district, pincode, contact, address, license, query)
    try:
        # raise NameError('HiThere')
        if request.POST.keys() != None:
            q = Query(
                name = name,
                company_name = company,
                state = state,
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
        
