from django.shortcuts import render

from shop.models import category,product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def base(request):
    return render(request,'base.html')

def allprodcat(request):
    c=category.objects.all()
    return render(request,'category.html',{'c':c})


def allproducts(request,cslug):
    c=category.objects.get(slug=cslug)
    p=product.objects.filter(category__slug=cslug)
    return render(request,'products.html',{'p':p,'c':c})

def prodetail(request,pslug):
    p=product.objects.get(slug=pslug)
    return render(request,'details.html',{'p': p})

def register(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if p==cp:
                us= User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
                us.save()
                return allprodcat(request)
    return render(request,'register.html')
def user_login(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        use=authenticate(username=u,password=p)
        if use:
            login(request,use)
            return allprodcat(request)
        else:
            messages.error(request,"invalid id")
    return render(request,'login.html')

def user_logout(request):
         logout(request)
         return allprodcat(request)




# get-otta element edikan
# filter oru sequence kitan