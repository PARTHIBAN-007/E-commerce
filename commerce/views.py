from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"shop/index.html")

def register(request):
    return render(request,"shop/register.html")

def collection(request):
    catagory = Catagory.objects.filter(status = 1)
    return render(request,"shop/collection.html", {"catagory":catagory})
    
    
def collectionview(request,name):
    if(Catagory.objects.filter(name=name,status = 1)):
        products= Product.objects.filter(category__name=name)
        return render(request,"shop/products/index.html", {"products":products,"category_name":name})
    else:
        messages.warning(request,"no such category found")
        return redirect('collectiion')
        
    
    