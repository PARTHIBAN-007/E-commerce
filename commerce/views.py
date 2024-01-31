from django.shortcuts import redirect, render
from . models import *
from commerce.form import customeruserform
from django.contrib import messages



# Create your views here
def home(request):
    products = Product.objects.filter(trending=1)
    return render(request,"shop/index.html", {"products":products})


def login_page(request):
    return render(request,"shop/login.html")

def register(request):
    form=customeruserform()
    if request.method=='POST':
        form=customeruserform(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request,"registeration success")
            
        
    return render(request,"shop/register.html",{"form": form })

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
        
    