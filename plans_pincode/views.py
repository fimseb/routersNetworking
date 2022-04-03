from django.http.response import JsonResponse
# from django.shortcuts import render
# import pandas,json

# Create your views here.
def get_plans(request):
    city_name = request.GET['city']
    print('------------------------------------------> city name : ', city_name)
    excel_data_df = pandas.read_excel('media/excel files/{city}.xlsx'.format(city=city_name), sheet_name='Sheet1')
    json_str = excel_data_df.to_json()
    json_data = json.loads(json_str)
    print('Excel Sheet to JSON:\n', json_data, '\n excel data : \n',excel_data_df)
    print('\n result :', json_data.keys())
    return JsonResponse(json_data, safe=False)

def get_plans_card(request, city):
    return JsonResponse()

def get_pincode(request):
    # excel2json.convert_from_file('pincode.xlsx')
    # form_pincode = request.GET['city']
    # print('--------------------------> city', form_pincode)
    pincode_form_value = str(request.GET['pincode'])
    # excel_data_df = pandas.read_excel('media/excel files/pincode.xlsx', sheet_name='Sheet1')
    # json_str = excel_data_df.to_json()
    # json_data = json.loads(json_str)
    # json_data = list(json_data.get('pincode').values())
    # result = pincode_form_value in json_data 

    data = open('media/json/pincode.json').read()
    data = json.loads(data)
    pincode_data = list(data.keys())
    # print('----------------------------------------------> data : ', pincode_data, '\n', 
    #         data['pincode'][0].get(str(pincode_form_value), '')
    #     )
    print('------------------------------------> pincode ', pincode_data, pincode_form_value)
    if pincode_form_value in pincode_data:
        response_data = {'valid' : True, 
                        'location' : list(data[pincode_form_value]['area'].keys())
        }
    else :
        response_data = {'valid':False}

    print('-------------------------------> response_data', response_data)
    # print('------------------------>', result, type(json_data[0]), type(pincode_form_value))
    return JsonResponse(response_data, safe=False)