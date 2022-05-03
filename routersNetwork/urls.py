"""routersNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from routersNetworkHtmlPages import views
# from routersNetworkHtmlPages import
from routersNetworkHtmlPages.download_csv_file import GenerateExcel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('', include('routersNetworkHtmlPages.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('routersNetworking_backend.urls')),
    # path('api-auth/', include('rest_framework.urls'))
    path('export/', GenerateExcel, name="export-excel")
]
