from django.urls import path
from . import views

urlpatterns = [

 #  for index (or) Home page
 path('', views.index ,name= 'index'),
 path('index/', views.index ,name= 'index'),
 path('home/', views.index ,name= 'index'),

 # for collections
 path('collections/', views.collections ,name= 'collections'),
 path('collections/<str:name>', views.collections_views ,name= 'collections'),
 path('collections/<str:cname>/<str:pname>', views.product_details ,name= 'product_details'),

 # foe registration
 path('register/', views.register ,name= 'register'),

 #pay
 path('AddToCart/', views.Add_To_Cart ,name= 'AddToCart'),
 path('cart/', views.cart ,name= 'cart'),

 #Delete
 path('ca_delete/<id>', views.ca_delete ,name= 'ca_delete'),
]