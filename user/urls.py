
from django.urls import path
from .import views

urlpatterns = [
    path('',views.landingpage,name="landingpage"),
    path('shop-grid',views.shopgrid,name="shopgrid"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('contact',views.contacts,name="contact"),
    path('product-details',views.productdetails,name="productdetails"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('checkout-details-add',views.landingpage,name="checkoutdetailsadd"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),

]
