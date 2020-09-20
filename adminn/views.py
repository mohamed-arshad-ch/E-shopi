from django.shortcuts import render
from user import models
# Create your views here.

def dashboard(request):
    return render(request,'default dashbord/dashboard_d.html')

def orders(request):
    
    return render(request,'default dashbord/orders.html')
    
def products(request):
    pass

def categories(request):
    pass