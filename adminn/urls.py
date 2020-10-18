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
    path('productdelete/<int:id>/',views.productdelete,name="productdelete"),
    path('categorysortadmin/<int:id>/',views.categorysortadmin,name="categorysortadmin"),
    path('statuschange/<int:id>',views.statuschange,name="statuschange"),
    path('prstatus/<int:id>/<str:sts>/',views.prostatus,name="prostatus"),
    path('users',views.users,name="users"),
    path('useredit/<int:id>',views.useredit,name="useredit"),
    
   

]