
from django.urls import path
from .import views

urlpatterns = [
    path('',views.landingpage,name="landingpage"),
    path('shop-grid',views.shopgrid,name="shopgrid"),
    path('cart',views.landingpage,name="cart"),
    path('checkout',views.landingpage,name="checkout"),
    path('contact',views.landingpage,name="contact"),
    path('product-details',views.landingpage,name="productdetails"),
    path('wishlist',views.landingpage,name="wishlist"),
    path('checkout-details-add',views.landingpage,name="checkoutdetailsadd"),
    path('login',views.landingpage,name="login"),
    path('register',views.landingpage,name="register"),

]
