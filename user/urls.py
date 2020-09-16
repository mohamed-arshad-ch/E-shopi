from django.contrib import admin
from django.urls import path,include
from user import urls
from views import landingpage

urlpatterns = [
    path('',views.landingpage,name="landingpage"),
    
]
