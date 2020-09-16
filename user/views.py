from django.shortcuts import render,HttpResponse

# Create your views here.
def landingpage(request):
    return render(request,'user/index.html')
