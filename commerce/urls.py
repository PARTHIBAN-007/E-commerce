from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('collection',views.collection,name="collection"),
    path('collection/<str:name>',views.collectionview,name="collection"),
    
    
]