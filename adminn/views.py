from django.shortcuts import render, redirect
from user.models import *
from django.contrib import messages
import datetime
from datetime import date
from django.core.files.storage import FileSystemStorage
import base64
from PIL import Image
from base64 import decodestring
import binascii
from django.core.files import File
from django.core.files.base import ContentFile

# Create your views here.


def adminlogin(request):

    if request.method == 'GET':

        response = render(request, 'default dashbord/login.html')
        response.set_cookie('username', "", max_age=25874577)
        na = request.COOKIES['username']
        if na == "admin":
            return redirect('dashboard')
        else:
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
                    response.set_cookie('username', username, max_age=25874577)
                    return response
                else:
                    messages.info(request, 'Invalid Password')
                    return redirect('adminlogin')
            else:

                return render(request, 'default dashbord/login.html')


def adminlogout(request):
    response = redirect('adminlogin')

    response.set_cookie('username', "")
    return response


def dashboard(request):

    na = request.COOKIES['username']
    if na == "admin":
        user = User.objects.filter(is_staff=True).count()

        customer = Customer.objects.count()

        queryset = OrderItem.objects.filter(complete=True)
        # df = queryset.count()
        # print(df)
        a = 0
        for j in queryset:
            a = a + 1
            print(j)
        print(a)
        n = 0
        qtyy = 0
        main = 0
        products = Product.objects.all()
        totqty = 0
        for pro in products:
            print("product", pro.qty)

            totqty = totqty + pro.qty
        print("product", totqty)

        for fff in queryset:
            n = n + fff.product.price
            qtyy = qtyy + fff.quantity
            print(fff.product.price)
            print(fff.quantity)
            print("------------------")

            total = fff.product.price * fff.quantity
            main = main + total
            print(main)
        print(main)
        print("lose", qtyy)
        print("in", totqty)
        last = totqty - qtyy
        active = 1
        return render(request, 'default dashbord/dashboard_d.html', {'users': user, 'order': a, 'total': main, 'last': last,'active':active})
    else:
        return redirect('adminlogin')


def orders(request):

    projects = OrderItem.objects.select_related('order').filter(complete=True)
    active = 2
    return render(request, 'default dashbord/orders.html', {'order': projects,'active':active})


def products(request):
    cate = Category.objects.all()
    product = Product.objects.all()
    active = 3
    return render(request, 'default dashbord/product.html', {'product': product, 'cat': cate,'active':active})


def categories(request):
    category = Category.objects.all()
    active = 4
    return render(request, 'default dashbord/category.html', {'category': category,'active':active})


def cateditview(request, id):
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
        return render(request, 'default dashbord/category-edit.html', {'category': category, 'key': "Update",'active':4})


def addcategory(request):
    if request.method == 'POST':
        name = request.POST['cname']
        description = request.POST['desc']

        category, created = Category.objects.get_or_create(
            cname=name, description=description)
        return redirect('category')
    else:
        return render(request, 'default dashbord/category-edit.html', {'key': "Add",'active':4})


def deletecategory(request, id):
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
        pic = request.POST['imagebase']

        format, imgstr = pic.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        cr = Category.objects.get(cname=cate)

        product = Product.objects.create(
            name=pname, cname=cr, description=description, price=price, qty=qty, image=data)
        return redirect('product')
    else:

        return render(request, 'default dashbord/product-edit.html', {'cat': category, 'key': "Add",'active':3})


def productedit(request, id):
    category = Category.objects.all()
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        pname = request.POST['pname']
        description = request.POST['desc']
        cate = request.POST['category']
        print(cate)
        price = request.POST['price']
        qty = request.POST['qty']
        pic = request.POST['imagebase']

        format, imgstr = pic.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        cg = Category.objects.get(cname=cate)

        product.name = pname
        product.description = description
        product.cname = cg
        product.price = price
        product.qty = qty
        product.image = data

        product.save()
        return redirect('product')
    else:

        return render(request, 'default dashbord/product-edit.html', {'cat': category, 'key': "Update", 'product': product,'active':3})


def productdelete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product')


def categorysortadmin(request, id):
    cate = Category.objects.all()
    catei = Category.objects.get(id=id)

    product = Product.objects.filter(cname=catei)

    return render(request, 'default dashbord/product.html', {'product': product, 'cat': cate})


def statuschange(request, id):
    order = Order.objects.get(id=id)
    orderitem = OrderItem.objects.filter(order=order, complete=True)
    active = 2
    return render(request, 'default dashbord/statuschange.html', {'orderitem': orderitem,'active':active})



    


def prostatus(request , id , sts ):
    orderitem = OrderItem.objects.get(id=id)
    orderitem.status_track = sts
    orderitem.save()
    return redirect('/orders')

def users(request):
    user = User.objects.all()
    active = 5
    return render(request, 'default dashbord/userlist.html', {'users': user,'active':active})


def useredit(request, id):
    user = User.objects.get(id=id)

    if user.is_staff == True:
        user.is_staff = False
        user.save()
        return redirect('users')
    else:
        user.is_staff = True
        user.save()
        return redirect('users')
