from django.contrib import admin
from .models import contact_form_details
# Register your models here.

class contact_form_detailsAdmin(admin.ModelAdmin):
    list_display = ['name','contact', 'email', 'message','is_contacted']
    
admin.site.register(contact_form_details, contact_form_detailsAdmin)