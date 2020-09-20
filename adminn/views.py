from django.shortcuts import render
from user.models import *

# Create your views here.

def dashboard(request):
    return render(request,'default dashbord/dashboard_d.html')

def orders(request):
    order = Order.objects.all()
    

    
    
    return render(request,'default dashbord/orders.html',{'order':order})
    
def products(request):
    pass

def categories(request):
    pass