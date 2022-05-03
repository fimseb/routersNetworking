# from sre_parse import State
from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Testimonial)
admin.site.register(State)
admin.site.register(District)
admin.site.register(News)
admin.site.register(Query)
admin.site.register(Subscribe)
admin.site.register(DOT)


