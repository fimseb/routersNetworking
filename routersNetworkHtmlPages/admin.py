
# from sre_parse import State   

from django.contrib import admin
# from matplotlib.pyplot import cla
from .models import *
from routersNetworkHtmlPages.download_csv_file import GenerateExcel



class QueryAdmin(admin.ModelAdmin):
    list_display=['query_id', 'name', 'company_name', 'state', 'district', 'pincode', 'contact', 'address', 'license', 'query_msg', 'date', 'time', 'query_assign_to_user_id', 'query_assign_by_user_id' ]
    actions = [GenerateExcel]

admin.site.register(Testimonial)
admin.site.register(State)
admin.site.register(District)
admin.site.register(News)
admin.site.register(Query, QueryAdmin)
admin.site.register(Subscribe)
admin.site.register(DOT)


