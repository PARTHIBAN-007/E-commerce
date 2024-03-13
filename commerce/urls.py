from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),   
    path('collection',views.collection,name="collection"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('collection/<str:name>',views.collectionview,name="collection"),
    path('collection/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('login',views.login_page,name="login_page")
    
    
]