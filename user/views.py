from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
import requests
from django.conf import settings
from django.contrib.auth import load_backend, login
import json
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password


# Create your views here.
f = ""

def landingpage(request):
    global f
    print(f)
   
    # print(request.user.first_name)
    # if request.user.is_authenticated:
    #     device = request.COOKIES['device']
    #     cust = Customer.objects.get(device=device)

    #     cust.user = request.user
    #     cust.name = request.user.first_name
    #     cust.save()
    #     products = Product.objects.all()
    #     response = render(request, 'user/index.html', {'products': products})
    #     response.set_cookie('java-tutorial', 'javatpoint.com')
    # else:
    # user = User.objects.get(username="rajav")
    # print(hash(user.password))
    # print(check_password("123",user.password))
    
    products = Product.objects.all()
    response = render(request, 'user/index.html', {'products': products})
    response.set_cookie('java-tutorial', 'javatpoint.com')

    return response


def shopgrid(request):

    
    products = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'user/category.html', {'products': products, 'category': category})

    
def categorysort(request,name):
    cat = Category.objects.get(cname=name)
    category = Category.objects.all()
    products = Product.objects.filter(cname=cat).values()
    
    return render(request, 'user/filtercategory.html', {'products': products, 'category': category})
    


def cart(request):
    if request.user.is_authenticated:

        # print("cx")
        user = User.objects.get(username=request.user)
        # print(request.user.username)
        # print(user.username)
        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)

        # queryset = Order.objects.filter(id=14).select_related('customer')
        # for g in queryset:
        #     print(g.customer)
        # fg = Order.objects.filter(customer='ch')

        context = {'order': order}

        return render(request, 'user/cart.html', context)
    else:
        try:
            customer = request.user.customer
            # print(customer)
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        # print(request.user)

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        context = {'order': order}

        return render(request, 'user/cart.html', context)

    # 	try:
    #     customer = request.user.customer
    # except:
    #     device = request.COOKIES['device']
    #     customer, created = Customer.objects.get_or_create(device=device)

    # order, created = Order.objects.get_or_create(
    #     customer=customer, complete=False)

    # context = {'order': order}
    # return render(request, 'user/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        # print(request.user.username)
        # print(user.username)
        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)

        # queryset = Order.objects.filter(id=14).select_related('customer')
        # for g in queryset:
        #     print(g.customer)
        # fg = Order.objects.filter(customer='ch')

        context = {'order': order}

        return render(request, 'user/checkout.html', context)
    else:
        try:
            customer = request.user.customer
            # print(customer)
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        # print(request.user)

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        context = {'order': order}

        return render(request, 'user/checkout.html', context)


def contacts(request):
    return render(request, 'user/contact.html')


def productdetails(request, pk):

    product = Product.objects.get(id=pk)
    device = request.COOKIES['device']

    # if request.user.is_authenticated:
    #     cust = Customer.objects.get(user=request.user)
    #     order = Order.objects.get(customer=cust)
    #     if request.method == 'POST':

    #         orderItem, created = OrderItem.objects.get_or_create(
    #             order=order, product=product)
    #         orderItem.quantity = request.POST['qty']
    #         orderItem.save()

    #         return redirect('cart')

    if request.method == 'POST':
        pass
        if request.user.is_authenticated:
            try:
                customer = request.user.customer
            except:
                device = request.COOKIES['device']
                customer = Customer.objects.get(
                     user=request.user)

            device = request.COOKIES['device']
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)

            order.device = device
            order.save()
            orderItem, created = OrderItem.objects.get_or_create(
                order=order, product=product)
            orderItem.quantity = request.POST['qty']
            orderItem.save()

            return redirect('cart')
        else:
            product = Product.objects.get(id=pk)
            # Get user account information
            try:
                customer = request.user.customer
            except:
                device = request.COOKIES['device']
                customer, created = Customer.objects.get_or_create(
                    device=device)

            device = request.COOKIES['device']
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)

            order.device = device
            order.save()
            orderItem, created = OrderItem.objects.get_or_create(
                order=order, product=product)
            orderItem.quantity = request.POST['qty']
            orderItem.save()

            return redirect('cart')

    else:
        context = {'product': product}
        return render(request, 'user/product-details.html', context)


def add_wishlist(request, id):
    if request.user.is_authenticated:

        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        product = Product.objects.get(id=id)

        print(product.name)
        print(product.image)

        wishlist, created = Wishlist.objects.get_or_create(user=request.user,
                                                           product_id=product.id, customer=customer, name=product, price=product.price, image=product.image)

        return redirect('landingpage')
    else:
        return redirect('login')
        # try:
        #     customer = request.user.customer
        # except:
        #     device = request.COOKIES['device']
        #     customer, created = Customer.objects.get_or_create(device=device)

        # product = Product.objects.get(id=id)

        # print(product.name)
        # print(product.image)

        # wishlist, created = Wishlist.objects.get_or_create(
        #     product_id=product.id, customer=customer, name=product, price=product.price, image=product.image)

        # return redirect('landingpage')


def wishlist(request):
    if request.user.is_authenticated:
        try:
            # customer = request.user.customer
            print(request.user)
        except:
            device = request.COOKIES['device']
            customer = Customer.objects.get(device=device)
        user = User.objects.get(username=request.user)
        customer = Customer.objects.get(user=user)

        wishlist = Wishlist.objects.all()

        return render(request, 'user/wishlist.html', {'wishlist': wishlist})

    else:
        return redirect('login')
        # try:
        #     customer = request.user.customer
        # except:
        #     device = request.COOKIES['device']
        #     customer, created = Customer.objects.get_or_create(device=device)

        # wishlist = Wishlist.objects.all()
        # return render(request, 'user/wishlist.html', {'wishlist': wishlist, 'customer': customer})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        request.session['team'] = username

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            device = request.COOKIES['device']

            # order = Order.objects.update_or_create(customer=username,device=device)

            de = Customer.objects.get(name=user.first_name)

            # order = Order.objects.get(device=device)
            # order.customer = request.user
            # order.save()
            # order, created = Order.objects.get_or_create(customer=request.user)
            # print(request.user)

            auth.login(request, user)

            # order, created = Order.objects.get_or_create(customer=customer)
            # order, created = Order.objects.get_or_create(customer=customer)
            # print(user.username,user.email,user.firstname)

            print(de.name)

            # order = Order.objects.get(customer=de)
            # if order is not None:
            #     order.customer = de
            #     order.complete = False
            #     order.transaction_id = 1254
            #     order.save()
            # else:
            #     print("Not Items")

            # wish = Wishlist.objects.get(customer=de)

            # if wish > 0:
            #     wish.user = request.user
            #     wish.save()
            #     return redirect('landingpage')
            # else:
            #     return redirect('landingpage')

            # customer.user = user.username

            # customer.email = user.email
            # customer.save()
            messages.info(request, 'Login Successfully')
            return redirect('landingpage')
            # return redirect('landingpage')

        else:
            print("loging rror")
            messages.info(request, 'Login Error')
            return redirect('login')

    # else:
    #     print("Login Error")
    #     #return render(request,'login.html')
    #     raise Http404("No user matches the given query.")

    else:
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        global f 
        f = password
        print(f)
        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=fname,last_name=phone)
        device = request.COOKIES['device']
        # customer, created = Customer.objects.get_or_create(user=user.username,name=fname,email=email,device=device)
        # userdata = User.objects.get(username=username)
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(
            device=device)
        customer = Customer.objects.get(device=device)

        customer.user = user
        # customer.name = user.firstname

        customer.name = fname
        customer.email = email
        customer.device = device
        customer.save()

        return redirect('login')

    else:
        return render(request, 'user/register.html')


def logout(request):
    auth.logout(request)

    response = redirect('payment')

    response.delete_cookie('device')
    response.delete_cookie('java-tutorial')

    return response


def payment(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        # print(request.user.username)
        # print(user.username)
        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)
        return render(request, 'user/payment.html', {'order': order})
    else:
        return redirect('login')


def otp(request):
    if request.method == 'GET':
        # phone = request.session['phone']
        phone = request.COOKIES['phone']
        url = "https://d7networks.com/api/verifier/send"
        number = str(91)+phone

        print(number)


        payload = {'mobile': number,
                   'sender_id': 'SMSINFO',
                   'message': 'Your otp code is {code}',
                   'expiry': '900'}

        headers = {
            'Authorization': 'Token c097fbd6e2a9e7f72d34f580086f726fd61c5108'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        
        id_nor = response.text[11:47]
        # print(id_nor)

        
        # a = []
        # print(response.text)
        # print(len(response.text))
        # for k in response.text:
        #     j = []
        #     j.insert(200,k)
        #     print(j)

        # a.append(j)
        # print(a)
        


        return render(request, 'user/verification.html',{'id':id_nor})
        

    else:
        
        otp_n = request.POST['otp_id']
        one = request.POST['one']
        two = request.POST['two']
        three = request.POST['three']
        four = request.POST['four']
        five = request.POST['five']

        six = request.POST['six']

        otp = one+two+three+four+five+six

        url = "https://d7networks.com/api/verifier/verify"

        payload = {'otp_id': otp_n,
                   'otp_code': otp}

        headers = {
            'Authorization': 'Token c097fbd6e2a9e7f72d34f580086f726fd61c5108'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        b = json.loads(response.text)
        print(b["status"])
        # phone = request.session['phone']
        global f
        print(f)
        phone = request.COOKIES['phone']
        if b["status"] == 'success':
            userdata = User.objects.get(last_name=phone)
            print(userdata.username)
            print(userdata.password)
            
            # if not hasattr(userdata, 'backend'):
            #     for backend in settings.AUTHENTICATION_BACKENDS:
            #         if userdata == load_backend(backend).get_user(userdata.pk):
            #             userdata.backend = backend
            #             break
            #             return redirect('landingpage')
            #         if hasattr(userdata, 'backend'):
            #             return login(request, userdata)
            #             return redirect('landingpage')
            
            user = auth.authenticate(username=userdata.username,password=userdata.passw)
            if user is not None:
                auth.login(request,user)
                print(response.text.encode('utf8'))
                messages.info(request, 'Login Successfully')
                return redirect('landingpage')
            else:
                messages.info(request, 'The Otp Is Not Ready')
                return redirect('landingpage')

            
            

            
        else:
            return redirect('login')


def verify(request):

    if request.method == 'POST':
        phone = request.POST['phone']
        user = User.objects.filter(last_name=phone).exists()
        
        

        if not user:
            messages.info(request, 'Mobile Number Invalid ! Please Register Your Number')
            
            return redirect('verification')

            
        else:
            # request.session['phone'] = phone
            responce = redirect('otp')
            responce.set_cookie('phone', phone)
            return responce
            # return redirect('otp')

            

        
    else:
        return render(request, 'user/otpmobile.html')

    
def addcartfromland(request,id):
    
    device = request.COOKIES['device']

    # if request.user.is_authenticated:
    #     cust = Customer.objects.get(user=request.user)
    #     order = Order.objects.get(customer=cust)
    #     if request.method == 'POST':

    #         orderItem, created = OrderItem.objects.get_or_create(
    #             order=order, product=product)
    #         orderItem.quantity = request.POST['qty']
    #         orderItem.save()

    #         return redirect('cart')

    
    product = Product.objects.get(id=id)
    if request.user.is_authenticated:
        
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer = Customer.objects.get(
                     user=request.user)

        device = request.COOKIES['device']
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        order.device = device
        order.save()
        orderItem, created = OrderItem.objects.get_or_create(
            order=order, product=product)
        orderItem.quantity = 1
        orderItem.save()

        return redirect('cart')
    else:
        product = Product.objects.get(id=id)
            # Get user account information
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(
                    device=device)

        device = request.COOKIES['device']
        order, created = Order.objects.get_or_create(
                customer=customer, complete=False)

        order.device = device
        order.save()
        orderItem, created = OrderItem.objects.get_or_create(
            order=order, product=product)
        orderItem.quantity = 1
        orderItem.save()

        return redirect('cart')

def itemplus(request,id):

    orderitem = OrderItem.objects.get(id=id)
    orderitem.quantity = orderitem.quantity+1
    orderitem.save()
    return redirect('cart')

def itemminus(request,id):
    orderitem = OrderItem.objects.get(id=id)
    orderitem.quantity = orderitem.quantity-1
    orderitem.save()
    return redirect('cart')

def removewishlist(request,id):
    wishlist = Wishlist.objects.get(id=id)
    wishlist.delete()
    return redirect('wishlist')

def cartproductdelete(request,id):
    orderitem = OrderItem.objects.get(id=id)
    orderitem.delete()
    return redirect('cart')