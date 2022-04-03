from django.urls import path, include
from routersNetworkHtmlPages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('ISPservice/', views.ISP),
    path('telco/', views.telco),
    path('technical/', views.technical),
    path('news/', views.news),
    path('contact/', views.contact),
    path('district/', views.district),
    path('contact_form/', views.contact_form_data),

    path('test/', views.test),
   
#    [z-zA-Z0-9*]

#    (?P<year>[0-9]{4})
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)