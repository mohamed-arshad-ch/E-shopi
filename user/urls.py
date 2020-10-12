
from django.urls import path
from .import views

urlpatterns = [
    path('',views.landingpage,name="landingpage"),
    path('shop-grid',views.shopgrid,name="shopgrid"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('contact',views.contacts,name="contact"),
    path('product-details/<int:pk>/',views.productdetails,name="productdetails"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('checkout-details-add',views.checkout,name="checkoutdetailsadd"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('addwishlist/<int:id>/',views.add_wishlist,name="addwishlist"),
    path('logout',views.logout,name="logout"),
    path('payment',views.payment,name="payment"),
    path('otp',views.otp,name="otp"),
    path('verification',views.verify,name="verification"),
    path('addcartfromland/<int:id>/',views.addcartfromland,name="addcartfromland"),
    path('categorysort/<str:name>/',views.categorysort,name="categorysort"),
    path('itemplus/<int:id>/',views.itemplus,name="itemplus"),
    path('itemminus/<int:id>/',views.itemminus,name="itemminus"),
    path('removewishlist/<int:id>',views.removewishlist,name="removewishlist"),
    path('cartproductdelete/<int:id>',views.cartproductdelete,name="cartproductdelete"),

    path('savebook/',views.AjaxHandler.as_view()),

    path('shippinaddress/',views.ShippingWalidation.as_view()),

    path('otpview/',views.OtpView.as_view()),
    path('orderproceed/',views.dfg,name="orderproceed"),
    path('orderhistory',views.orderhistory,name="orderhistory"),
    path('getshipping/',views.Getshipping.as_view()),
   


]
