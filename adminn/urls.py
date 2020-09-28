from django.urls import path
from .import views

urlpatterns = [
    path('logic',views.adminlogin,name="adminlogin"),
    path('adminlogout',views.adminlogout,name="adminlogout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('orders',views.orders,name="orders"),
    path('product',views.products,name="product"),
    path('category',views.categories,name="category"),
    path('addcategory',views.addcategory,name="addcategory"),
    
    path('categoryedit/<int:id>/',views.cateditview,name="categoryedit"),
    path('categorydelete/<int:id>/',views.deletecategory,name="categorydelete"),

    path('productadd',views.productadd,name="productadd"),
    path('productedit/<int:id>/',views.productedit,name="productedit"),
    path('productdelete/<int:id>/',views.productdelete,name="productdelete")
   

]