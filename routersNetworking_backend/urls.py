# from django.contrib import admin
from django.urls import path
from routersNetworking_backend import views
# from routersNetworkHtmlPages import

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('add_state/', views.add_state_api),
    path('add_district/',views.add_district_api),
    # path('add_distict',views.add_district_api),

    # Token Authentication URL
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

