from django.urls import path
from .import views

urlpatterns = [
    path('logic',views.dashboard,name="dashboard"),
    path('orders',views.orders,name="orders"),
    path('product',views.dashboard,name="product"),
    path('category',views.dashboard,name="category"),
   

]