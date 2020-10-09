from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
import requests
from django.http import JsonResponse
from time import time
from django.conf import settings
from django.contrib.auth import load_backend, login
import json
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from django.views.generic import View

# Create your views here.
f = ""


def landingpage(request):

    if request.user.is_authenticated:

        user = User.objects.get(username=request.user)

        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)

        queryset = OrderItem.objects.filter(order=order, complete=False)

        print(queryset)
        df = queryset.count()

        print("-------------------")
        print(df)
        print("-------------------")
        cartItems = df
        context = {'order': order, 'cartItems': cartItems}

    else:
        try:
            customer = request.user.customer

        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        queryset = OrderItem.objects.filter(order=order)
        df = queryset.count()
        print("-------------------")
        print(df)
        print("-------------------")
        cartItems = df
        context = {'order': order, 'cartItems': cartItems}

    products = Product.objects.all()
    response = render(request, 'user/index.html',
                      {'products': products, 'cartItems': cartItems})
    response.set_cookie('java-tutorial', 'javatpoint.com')

    return response


def shopgrid(request):

    products = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'user/category.html', {'products': products, 'category': category})


def categorysort(request, name):
    cat = Category.objects.get(cname=name)
    category = Category.objects.all()
    products = Product.objects.filter(cname=cat).values()

    return render(request, 'user/filtercategory.html', {'products': products, 'category': category})


def cart(request):
    if request.user.is_authenticated:

        user = User.objects.get(username=request.user)

        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)

        queryset = OrderItem.objects.filter(order=order, complete=False)
        df = queryset.count()

        cartItems = df
        a = 0
        qtyy = 0
        main = 0
        for fff in queryset:
            a = a + fff.product.price
            qtyy = qtyy + fff.quantity
            print(fff.product.price)
            print(fff.quantity)
            print("------------------")

            total = fff.product.price * fff.quantity
            main = main + total
            print(main)

        print(main)

        context = {'order': order, 'cartItems': cartItems, 'tot': main}

        return render(request, 'user/cart.html', context)
    else:
        try:
            customer = request.user.customer

        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        queryset = OrderItem.objects.filter(order=order)
        df = queryset.count()
        print("-------------------")
        print(df)
        print("-------------------")
        cartItems = df
        a = 0
        qtyy = 0
        main = 0
        for fff in queryset:
            a = a + fff.product.price
            qtyy = qtyy + fff.quantity
            print(fff.product.price)
            print(fff.quantity)
            print("------------------")

            total = fff.product.price * fff.quantity
            main = main + total
            print(main)

        print(main)

        context = {'order': order, 'cartItems': cartItems, 'tot': main}
        return render(request, 'user/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)

        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)

        queryset = OrderItem.objects.filter(order=order, complete=False)
        df = queryset.count()
        shipping = ShippingAddress.objects.filter(customer=customer)

        cartItems = df
        a = 0
        qtyy = 0
        main = 0
        for fff in queryset:
            a = a + fff.product.price
            qtyy = qtyy + fff.quantity
            print(fff.product.price)
            print(fff.quantity)
            print("------------------")

            total = fff.product.price * fff.quantity
            main = main + total
            print(main)

        print(main)

        context = {'order': order, 'cartItems': cartItems,
                   'tot': main, 'ship': shipping}

        return render(request, 'user/checkout.html', context)
    else:
        try:
            customer = request.user.customer

        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        queryset = OrderItem.objects.filter(order=order)
        df = queryset.count()
        print("-------------------")
        print(df)
        print("-------------------")
        cartItems = df
        a = 0
        qtyy = 0
        main = 0
        for fff in queryset:
            a = a + fff.product.price
            qtyy = qtyy + fff.quantity
            print(fff.product.price)
            print(fff.quantity)
            print("------------------")

            total = fff.product.price * fff.quantity
            main = main + total
            print(main)

        print(main)

        context = {'order': order, 'cartItems': cartItems, 'tot': main}

        return render(request, 'user/checkout.html', context)


def contacts(request):
    return render(request, 'user/contact.html')


def productdetails(request, pk):

    product = Product.objects.get(id=pk)
    device = request.COOKIES['device']

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


def wishlist(request):
    if request.user.is_authenticated:
        try:

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


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        request.session['team'] = username

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff == True:

                device = request.COOKIES['device']

                de = Customer.objects.get(name=user.first_name)

                auth.login(request, user)

                print(de.name)

                messages.info(request, 'Login Successfully')
                return redirect('landingpage')
            else:
                messages.info(request, 'The User Is Dectivate Please Contact')
                return redirect('login')


        else:
            print("loging rror")
            messages.info(request, 'Login Error')
            return redirect('login')

    else:
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        otp = request.POST['otp']

        otp_n = request.COOKIES['tp_id']
        url = "https://d7networks.com/api/verifier/verify"

        payload = {'otp_id': otp_n,
                   'otp_code': otp}

        headers = {
            'Authorization': 'Token c38a9193a40ae757a14ab1aacd2345d019e3c50e'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        b = json.loads(response.text)
        print(b["status"])

        phone = request.COOKIES['phone']
        if b["status"] == 'success':
            user = User.objects.create_user(
                username=username, email=email, password=password, first_name=fname, last_name=phone,is_staff=True)
            device = request.COOKIES['device']

            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(
                device=device)
            customer = Customer.objects.get(device=device)

            customer.user = user

            customer.name = fname
            customer.email = email
            customer.device = device
            customer.save()

            user_otp = Userotp.objects.create(
                name=user, phone=phone, passw=password)
            userdata = User.objects.get(last_name=phone)
            print(userdata.username)
            print(userdata.password)
            user_otp = Userotp.objects.get(name=userdata)

            user = auth.authenticate(
                username=userdata.username, password=user_otp.passw)
            if user is not None:
                # auth.login(request, user)
                # print(response.text.encode('utf8'))
                # messages.info(request, 'Login Successfully')
                # return redirect('landingpage')
                if user.is_staff == True:

                    device = request.COOKIES['device']

                    de = Customer.objects.get(name=user.first_name)

                    auth.login(request, user)

                    print(de.name)

                    messages.info(request, 'Login Successfully')
                    return redirect('landingpage')
                else:
                    messages.info(request, 'The User Is Dectivate Please Contact')
                    return redirect('login')
            else:
                messages.info(request, 'The Otp Is Not Ready')
                return redirect('landingpage')

        else:
            return redirect('login')

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

        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)
        user = User.objects.get(username=request.user)

        queryset = OrderItem.objects.filter(order=order, complete=False)
        df = queryset.count()

        cartItems = df
        a = 0
        qtyy = 0
        main = 0
        for fff in queryset:
            a = a + fff.product.price
            qtyy = qtyy + fff.quantity
            print(fff.product.price)
            print(fff.quantity)
            print("------------------")

            total = fff.product.price * fff.quantity
            main = main + total
            print(main)

        print(main)

        context = {'order': order, 'cartItems': cartItems, 'tot': main}
        return render(request, 'user/payment.html', context)
    else:
        return redirect('login')


def otp(request):
    if request.method == 'GET':

        phone = request.COOKIES['phone']
        url = "https://d7networks.com/api/verifier/send"
        number = str(91)+phone

        print(number)

        payload = {'mobile': number,
                   'sender_id': 'SMSINFO',
                   'message': 'Your otp code is {code}',
                   'expiry': '900'}

        headers = {
            'Authorization': 'Token c38a9193a40ae757a14ab1aacd2345d019e3c50e'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        id_nor = response.text[11:47]

        return render(request, 'user/verification.html', {'id': id_nor})

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
            'Authorization': 'Token c38a9193a40ae757a14ab1aacd2345d019e3c50e'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        b = json.loads(response.text)
        print(b["status"])

        global f
        print(f)
        phone = request.COOKIES['phone']
        if b["status"] == 'success':
            userdata = User.objects.get(last_name=phone)
            print(userdata.username)
            print(userdata.password)
            user_otp = Userotp.objects.get(name=userdata)

            user = auth.authenticate(
                username=userdata.username, password=user_otp.passw)
            if user is not None:
                # auth.login(request, user)
                # print(response.text.encode('utf8'))
                # messages.info(request, 'Login Successfully')
                # return redirect('landingpage')
                if user.is_staff == True:

                    device = request.COOKIES['device']

                    de = Customer.objects.get(name=user.first_name)

                    auth.login(request, user)

                    print(de.name)

                    messages.info(request, 'Login Successfully')
                    return redirect('landingpage')
                else:
                    messages.info(request, 'The User Is Dectivate Please Contact')
                    return redirect('login')
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
            messages.info(
                request, 'Mobile Number Invalid ! Please Register Your Number')

            return redirect('verification')

        else:

            responce = redirect('otp')
            responce.set_cookie('phone', phone)
            return responce

    else:
        return render(request, 'user/otpmobile.html')


def addcartfromland(request, id):

    device = request.COOKIES['device']

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


def itemplus(request, id):

    orderitem = OrderItem.objects.get(id=id)
    orderitem.quantity = orderitem.quantity+1
    orderitem.save()
    return redirect('cart')


def itemminus(request, id):
    orderitem = OrderItem.objects.get(id=id)
    orderitem.quantity = orderitem.quantity-1
    orderitem.save()
    return redirect('cart')


def removewishlist(request, id):
    wishlist = Wishlist.objects.get(id=id)
    wishlist.delete()
    return redirect('wishlist')


def cartproductdelete(request, id):
    orderitem = OrderItem.objects.get(id=id)
    orderitem.delete()
    return redirect('cart')


def savebook(request):
    fname = request.GET['fname']

    print(fname)


class AjaxHandler(View):
    def get(self, request):
        print("Arshad In Get")

        if request.user.is_authenticated:

            user = User.objects.get(username=request.user)

            customer = Customer.objects.get(user=user)
            order = Order.objects.get(customer=customer)

            queryset = OrderItem.objects.filter(order=order)
            df = queryset.count()
            print(queryset)
            print("-------------------")
            print(df)
            print("-------------------")

            context = {'count': df}
            return JsonResponse({'count': df}, status=200)
            return render(request, 'user/base.html', context)
        else:
            try:
                customer = request.user.customer

            except:
                device = request.COOKIES['device']
                customer, created = Customer.objects.get_or_create(
                    device=device)

            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)

            queryset = OrderItem.objects.filter(order=order)
            df = queryset.count()
            print("-------------------")
            print(df)
            print("-------------------")
            context = {'count': df}

            return JsonResponse({'count': df}, status=200)

    def post(self, request):
        print("Arshad In Post")
        text1 = request.POST.get('product_id')
        print()
        print(text1)
        print()
        device = request.COOKIES['device']
        product = Product.objects.get(id=text1)
        if request.user.is_authenticated:

            try:
                customer = request.user.customer
            except:
                device = request.COOKIES['device']
                customer = Customer.objects.get(
                    user=request.user)

            device = request.COOKIES['device']
            order = Order.objects.get(
                customer=customer, complete=False)

            order.device = device
            order.save()
            orderItem, created = OrderItem.objects.get_or_create(complete=False, quantity=1,
                                                                 order=order, product=product)

            return redirect('cart')
        else:
            product = Product.objects.get(id=text1)

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


def co(request):
    if request.user.is_authenticated:

        user = User.objects.get(username=request.user)

        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)

        queryset = OrderItem.objects.filter(order=order)
        df = queryset.count()
        print("-------------------")
        print(df)
        print("-------------------")

        context = {'count': df}

        return render(request, 'user/base.html', context)
    else:
        try:
            customer = request.user.customer

        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        queryset = OrderItem.objects.filter(order=order)
        df = queryset.count()
        print("-------------------")
        print(df)
        print("-------------------")
        context = {'count': df}
        return render(request, 'user/cart.html', context)


class ShippingWalidation(View):

    def post(self, request):
        add1 = request.POST.get('ad1')
        add2 = request.POST.get('ad2')
        add3 = request.POST.get('ad3')
        city = request.POST.get('cityy')
        mob = request.POST.get('mobb')
        zipc = request.POST.get('zipp')

        print(add1, add2, add3, city, mob, zipc)

        user = User.objects.get(username=request.user)
        print(user)
        customer = Customer.objects.get(user=user)
        print(customer)
        order = Order.objects.get(customer=customer)

        shipping, created = ShippingAddress.objects.get_or_create(
            customer=customer, order=order, address1=add1, address2=add2, address3=add3, city=city, state=mob, zipcode=zipc)

        return redirect("/")


class OtpView(View):
    def post(self, request):
        phone = request.POST.get('phone')
        print(phone)

        url = "https://d7networks.com/api/verifier/send"
        number = str(91)+phone

        print(number)

        payload = {'mobile': number,
                   'sender_id': 'SMSINFO',
                   'message': 'Your otp code is {code}',
                   'expiry': '900'}

        headers = {
            'Authorization': 'Token c38a9193a40ae757a14ab1aacd2345d019e3c50e'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        id_nor = response.text[11:47]
        print(id_nor)
        responsed = redirect('/')
        responsed.set_cookie('tp_id', id_nor)
        responsed.set_cookie('phone', phone)

        return responsed


def dfg(request):
    user = User.objects.get(username=request.user)
    print(user)
    customer = Customer.objects.get(user=user)
    print(customer)
    order = Order.objects.get(customer=customer)
    print(order)
    orderitem = OrderItem.objects.filter(order=order)
    for i in orderitem:
        i.complete = True
        i.save()
    return redirect('landingpage')


def orderhistory(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)

        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer)

        queryset = OrderItem.objects.filter(order=order, complete=False)
        df = queryset.count()

        cartItems = df
        a = 0
        qtyy = 0
        main = 0
        for fff in queryset:
            a = a + fff.product.price
            qtyy = qtyy + fff.quantity
            print(fff.product.price)
            print(fff.quantity)
            print("------------------")

            total = fff.product.price * fff.quantity
            main = main + total
            print(main)

        print(main)

        context = {'order': order, 'cartItems': cartItems, 'tot': main}
        return render(request, 'user/orderhistory.html', context)
    else:
        return redirect('login')


class Getshipping(View):

    def get(self, request):
        text = request.GET.get('ship_id')
        print(text)

        shipi = ShippingAddress.objects.get(id=text)

        a = shipi.address1
        b = shipi.address2
        vb = {
            'address1': shipi.address1,
            'address2': shipi.address2,
            'address3': shipi.address3,
            'city': shipi.city,
            'mob': shipi.state,
            'zip': shipi.zipcode

        }
        return JsonResponse({'count2': vb}, status=200)
        return redirect('/')
