from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.add_contact_form_detail_db, name='contact'),
]