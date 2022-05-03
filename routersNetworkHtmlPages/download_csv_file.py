import csv
from routersNetworkHtmlPages.models import Query
import pandas as pd
from routersNetworkHtmlPages.serializers import QuerySerializer
import uuid
from django.http import HttpResponse
from django.shortcuts import redirect

from routersNetworkHtmlPages.serializers import QuerySerializer

class GenerateExcel:
    short_description = "Download in Excel Sheet"

    def __new__(cls, modeladmin, request, queryset):
        result = cls.generate_excel_sheet(modeladmin, request, queryset)
        return result

    @classmethod
    def generate_excel_sheet(cls, modeladmin, request, queryset):
        query_obj = Query.objects.all()
        fields = ['name', 'company_name', 'state', 'district', 'pincode', 'contact', 'address', 'license', 'query_msg', 'date', 'time']
        filename = "query_change.csv"
        rows = []
        for obj in query_obj:
            lis = []
            lis.append(str(obj.name))
            lis.append(str(obj.company_name))
            lis.append(str(obj.state))
            lis.append(str(obj.district))
            lis.append(str(obj.pincode))
            lis.append(str(obj.contact))
            lis.append(str(obj.address))
            lis.append(str(obj.license))
            lis.append(str(obj.query_msg))
            lis.append(str(obj.date))
            lis.append(str(obj.time))
            rows.append(lis)
            
        with open('media/excel/query.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        print('------------------> fields ', rows)
        # serializer = QuerySerializer(query_obj, many=True)
        # df = pd.DataFrame(query_obj)
        # print(df)
        # df.to_csv(f"media/excel/query.csv", encoding='UTF-8',index=False)
        return redirect('/media/excel/query.csv')
        # response = HttpResponse(content_type='text/csv',headers={'Content-Disposition': 'attachment; filename="/media/excel/query.csv"'},)

        # writer = csv.writer(response)
        # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
        
        # return HttpResponse(df, content_type='text/csv')

    