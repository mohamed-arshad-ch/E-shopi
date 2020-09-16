from django.shortcuts import render,HttpResponse

# Create your views here.
def landingpage(request):
    return render(request,'user/index.html')

def shopgrid(request):
    return render(request,'user/category.html')

def cart(request):
    return render(request,'user/cart.html')


def checkout(request):
    return render(request,'user/checkout.html')

def contacts(request):
    return render(request,'user/contact.html')

def productdetails(request):
    return render(request,'user/product-details.html')

def wishlist(request):
    return render(request,'user/wishlist.html')

def login(request):
    return render(request,'user/login.html')

def register(request):
    return render(request,'user/register.html')