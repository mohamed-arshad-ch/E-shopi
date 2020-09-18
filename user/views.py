from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def landingpage(request):
    products = Product.objects.all()
    
    return render(request,'user/index.html',{'products':products})

def shopgrid(request):
    products = Product.objects.all()
    category = Category.objects.all()
    return render(request,'user/category.html',{'products':products,'category':category})
    

def cart(request):
	try:
		customer = request.user.customer
	except:
		device = request.COOKIES['device']
		customer, created = Customer.objects.get_or_create(device=device)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	context = {'order':order}
	return render(request, 'user/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass
        else:
            try:
                customer = request.user.customer
            except:
                device = request.COOKIES['device']
                customer, created = Customer.objects.get_or_create(device=device)
            
            order, created = Order.objects.get_or_create(customer=customer,complete=False)
            return render(request,'user/checkout.html',{'order':order})
    #         try:
	# 	customer = request.user.customer
	# except:
	# 	device = request.COOKIES['device']
	# 	customer, created = Customer.objects.get_or_create(device=device)

	# order, created = Order.objects.get_or_create(customer=customer, complete=False)

	# context = {'order':order}
	# return render(request, 'user/cart.html', context)
        
    else:
        return render(request,'user/login.html')

    

def contacts(request):
    return render(request,'user/contact.html')



def productdetails(request, pk):
	product = Product.objects.get(id=pk)

	if request.method == 'POST':
		product = Product.objects.get(id=pk)
		#Get user account information
		try:
			customer = request.user.customer	
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
		orderItem.quantity=request.POST['qty']
		orderItem.save()

		return redirect('cart')

	context = {'product':product}
	return render(request, 'user/product-details.html', context)	

def add_wishlist(request,id):
	try:
		customer = request.user.customer
	except:
		device = request.COOKIES['device']
		customer, created = Customer.objects.get_or_create(device=device)

	
	product = Product.objects.get(id=id)
	
	print(product.name)
	print(product.image)

	wishlist, created = Wishlist.objects.get_or_create(product_id=product.id , customer=customer,name=product,price=product.price,image=product.image)

	
	return redirect('landingpage')
    
def wishlist(request):
	try:
		customer = request.user.customer
	except:
		device = request.COOKIES['device']
		customer, created = Customer.objects.get_or_create(device=device)
	
	
	wishlist = Wishlist.objects.all()
	return render(request,'user/wishlist.html',{'wishlist':wishlist,'customer':customer})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = User.objects.get(username=username)

		userlogin = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,userlogin)
			print(user.username)
			device = request.COOKIES['device']
			customer = Customer.objects.get(device=device)
			print(user.username,user.email,user.firstname)
			# customer.user = username
			customer.name = user.firstname
			customer.email = user.email
			customer.save()
			# customer.user = user.username
			# # customer.name = user.first_name
			# customer.email = user.email
			# customer.save()
			return redirect('landingpage')
            # return redirect('landingpage')
		else:
			print("loging rror")
			return render(request,'user/login.html')
			raise Http404("No User Match")
        # else:
        #     print("Login Error")
        #     #return render(request,'login.html')
        #     raise Http404("No user matches the given query.")

		
	else:
		return render(request,'user/login.html')


    

def register(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		user = User.objects.create(username=username,email=email,password=password,first_name=fname)

		return redirect('login')
		
	else:
		return render(request,'user/register.html')
	
    