from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
def landingpage(request):
    products = Product.objects.all()
    
    return render(request,'user/index.html',{'products':products})

def shopgrid(request):
    return render(request,'user/category.html')

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

def wishlist(request):
    return render(request,'user/wishlist.html')

def login(request):

    return render(request,'user/login.html')

def register(request):
    return render(request,'user/register.html')