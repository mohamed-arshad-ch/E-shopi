from django.shortcuts import render,redirect
from user.models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def adminlogin(request):


    if request.method == 'GET':
        response = render(request,'default dashbord/login.html')
        response.set_cookie('username', "",max_age=25874577)
        return response
        
    else:
        
        na = request.COOKIES['username']

        if na == "admin":
            return redirect('dashboard')
        else:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                if username == "admin" and password == "123":
                    response = redirect('dashboard')
                    response.set_cookie('username', username,max_age=25874577)
                    return response
                else:
                    messages.info(request, 'Invalid Password')
                    return redirect('adminlogin')
            else:
                
                return render(request,'default dashbord/login.html')
    

    
def adminlogout(request):
    response = redirect('adminlogin')

    response.set_cookie('username', "")
    return response


def dashboard(request):
    na = request.COOKIES['username']
    if na == "admin":
        return render(request,'default dashbord/dashboard_d.html')
    else:
        return redirect('adminlogin')
    

def orders(request):
    order = Order.objects.all()
    

    
    
    return render(request,'default dashbord/orders.html',{'order':order})
    
def products(request):

    product = Product.objects.all()
    return render(request,'default dashbord/product.html',{'product':product})

def categories(request):
    category = Category.objects.all()
    return render(request,'default dashbord/category.html',{'category':category})

def cateditview(request,id):
    if request.method == 'POST':
        name = request.POST['cname']
        description = request.POST['desc']
        category = Category.objects.get(id=id)

        category.cname = name
        category.description = description
        category.save()
        return redirect('category')
    else:
        category = Category.objects.get(id=id)
        return render(request,'default dashbord/category-edit.html',{'category':category,'key':"Update"})


def addcategory(request):
    if request.method == 'POST':
        name = request.POST['cname']
        description = request.POST['desc']

        category, created = Category.objects.get_or_create(cname=name,description=description) 
        return redirect('category')
    else:
        return render(request,'default dashbord/category-edit.html',{'key':"Add"})

def deletecategory(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category')


def productadd(request):
    category = Category.objects.all()
    if request.method == 'POST':
            pname = request.POST['pname']
            description = request.POST['desc']
            cate = request.POST['category']
            price = request.POST['price']
            qty = request.POST['qty']
            pic=request.FILES.get('myfile')

            cr = Category.objects.get(cname=cate)

            product = Product.objects.create(name=pname,cname=cr,description=description,price=price,qty=qty,image=pic)  
            return redirect('product') 
    else:

        return render(request,'default dashbord/product-edit.html',{'cat':category,'key':"Add"})


def productedit(request,id):
    category = Category.objects.all()
    product = Product.objects.get(id=id)


    if request.method == 'POST':
        pname = request.POST['pname']
        description = request.POST['desc']
        cate = request.POST['category']
        print(cate)
        price = request.POST['price']
        qty = request.POST['qty']
        pic=request.FILES.get('myfile')
        
        cg = Category.objects.get(cname=cate)

        product.name = pname
        product.description = description
        product.cname = cg
        product.price = price
        product.qty = qty
        product.image = pic

        product.save()
        return redirect('product')
    else:


        return render(request,'default dashbord/product-edit.html',{'cat':category,'key':"Update",'product':product})

def productdelete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product')
    
    



