from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('collection',views.collection,name="collection"),
    path('collection/<str:name>',views.collectionview,name="collection"),
    path('collection/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    
    
]