from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from shop.models import product
from cart.models import Cart,Account,Order


@login_required
def cart_view(request):
    total=0
    try:
        user=request.user
        cartitems=Cart.objects.filter(user=user)
        for i in cartitems:
            total+= i.quantity * i.products.price
    except Cart.DoesNotExist:
         pass
    return render(request,'cart.html',{'cart':cartitems,'total':total})



@login_required

def add_cart(request,p):
    product1= product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product1,user=user)
        if cart.quantity<cart.products.stock:
            cart.quantity+=1
            cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(products=product1,user=user,quantity=1)
        cart.save()

    return redirect('cart:cart_view')

@login_required
def cart_remove(request,p):
    product1=product.objects.get(id=p)
    user = request.user
    try:
        cart=Cart.objects.get(products=product1,user=user)
        if cart.quantity > 1:
                cart.quantity-=1
                cart.save()
        else:
                 cart.delete()
    except:
        pass
    return redirect('cart:cart_view')

@login_required
def full_remove(request,p):
    product1=product.objects.get(id=p)
    user = request.user
    try:
        cart=Cart.objects.get(products=product1,user=user)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')
@login_required
def order(request):
    total=0
    if request.method=="POST":
        x=request.POST['x']
        y = request.POST['y']
        z = request.POST['z']
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity * i.products.price

        ac=Account.objects.get(acctnumber=z)
        if float(ac.amount) >=total:
            ac.amount=ac.amount-total
            ac.save()
            for i in cart:
                o = Order.objects.create(user=user,products=i.products,address=x,phone=y,order_status="paid",
                                         no_of_items=i.quantity)
                o.save()
            cart.delete()
            msg="order placed successsfully"
            return render(request,'orderdetails.html',{'msg':msg,'total':total,'items':x})
            status="paid"
        else:
            msg="order cannot be placed"
            return render(request, 'orderdetails.html', {'msg': msg})
    return render(request,'accountform.html')
def orderview(request):
    user=request.user
    v = Order.objects.create(user=user,order_status="paid")
    return render (request,'orderview.html',{'v':v,'name':user.username})

# decorate function vechal login page kazhinje add_cart page varu
#product=Product.objects.get(id=p)
#ethu product aanu cart lewke add cheyunnathene
# user=request.user,  current user nte login details anu ithile
#redirect connect to views
#render will connect to html
#cartitems=Cart.Objects.create(products=product,user=user,quantity=1)  ithil redil kanathe table le fields anu

#iproducts, cartle 1st item thile product. .price means aa productnte price
#cart=Cart.objects.filter(user=user), Cart enna tablw nu currently login cheythirikuna user filter cheythu edukunu, ayalde cart input eduthu cart ena variable leke add cheyanu