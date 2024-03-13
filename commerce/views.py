from django.http import  JsonResponse
from django.shortcuts import redirect, render
from . models import *

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json


# Create your views here
def home(request):
    products = Product.objects.filter(trending=1)
    return render(request,"shop/index.html", {"products":products})



def cart_page(request):
  
    cart=Cart.objects.all()
    
    return render(request,"shop/cart.html",{"cart":cart})
 

def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")  
  
  
def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        
            data=json.load(request)
            product_id=data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(product_id=product_id):
                    return JsonResponse({'status':'Product Already in Favourite'}, status=200)
                else:
                    Favourite.objects.create(product_id=product_id)
                    return JsonResponse({'status':'Product Added to Favourite'}, status=200)
        
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)
 
 
 
def favviewpage(request):
  
    fav=Favourite.objects
    return render(request,"shop/fav.html",{"fav":fav})
  

def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")

def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    


def login_page(request):
    return render(request,"shop/login.html")
 


def collection(request):
    catagory = Catagory.objects.filter(status = 1)
    return render(request,"shop/collection.html", {"catagory":catagory})
    
    
def collectionview(request,name):
    if(Catagory.objects.filter(name=name,status = 1)):
        products= Product.objects.filter(category__name=name)
        # print(products)
        return render(request,"shop/products/index.html", {"products":products,"category_name":name})
    else:
        messages.warning(request,"no such category found")
        return redirect('collectiion')
        
def product_details(request,cname,pname):
    if (Catagory.objects.filter(name=cname,status=1)):
        if (Product.objects.filter(name=pname,status=1)):
            products = Product.objects.filter(name=pname,status=1).first()
            return render(request,"shop/products/productdetails.html", {"products":products})
        else:
            messages.error(request,"no such product is available")
            return redirect('collectiion')
    else:
        messages.error(request,"no such Category is available") 
        return redirect('collectiion')   
        
    