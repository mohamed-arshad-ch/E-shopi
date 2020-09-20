from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


def landingpage(request):
    products = Product.objects.all()
    response = render(request, 'user/index.html', {'products': products})  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    
    return response 

     


def shopgrid(request):
    products = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'user/category.html', {'products': products, 'category': category})


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
        if request.method == 'POST':
            pass
        else:
            try:
                customer = request.user.customer
            except:
                device = request.COOKIES['device']
                customer, created = Customer.objects.get_or_create(
                    device=device)

            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            return render(request, 'user/index.html', {'order': order})
    #         try:
        # 	customer = request.user.customer
        # except:
        # 	device = request.COOKIES['device']
        # 	customer, created = Customer.objects.get_or_create(device=device)

        # order, created = Order.objects.get_or_create(customer=customer, complete=False)

        # context = {'order':order}
        # return render(request, 'user/cart.html', context)

    else:
        return render(request, 'user/login.html')


def contacts(request):
    return render(request, 'user/contact.html')


def productdetails(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        # Get user account information
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

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

    context = {'product': product}
    return render(request, 'user/product-details.html', context)


def add_wishlist(request, id):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    product = Product.objects.get(id=id)

    print(product.name)
    print(product.image)

    wishlist, created = Wishlist.objects.get_or_create(
        product_id=product.id, customer=customer, name=product, price=product.price, image=product.image)

    return redirect('landingpage')


def wishlist(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    wishlist = Wishlist.objects.all()
    return render(request, 'user/wishlist.html', {'wishlist': wishlist, 'customer': customer})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userdata = User.objects.get(username=username)

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


            auth.login(request,user)
			
            
			
			# order, created = Order.objects.get_or_create(customer=customer)
            # order, created = Order.objects.get_or_create(customer=customer)
            # print(user.username,user.email,user.firstname)
            

            print(de.name)

            order = Order.objects.get(customer=de)
            order.customer = de
            order.complete = False
            order.transaction_id = 1254
            order.save()

			
			


            # customer.user = user.username

            # customer.email = user.email
            # customer.save()

            
            return redirect('landingpage')
            # return redirect('landingpage')
       

        else:
            print("loging rror")
            return render(request, 'user/login.html')
            raise Http404("No User Match")
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
        
        
        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=fname)
        device = request.COOKIES['device']
        # customer, created = Customer.objects.get_or_create(user=user.username,name=fname,email=email,device=device)
        # userdata = User.objects.get(username=username)

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
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)
    customer.device=''
    customer.save() 
    response = redirect('/') 
    de = Customer.objects.get(device=device)
    de.delete()
    response.delete_cookie('device') 
    
    
    
    
    return response 