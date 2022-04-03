from django.urls import path, include
from . import views
urlpatterns = [
    path('plans/', views.get_plans_card),
    path('viewplan/', views.get_plans),
    path('pincode/', views.get_pincode),
]