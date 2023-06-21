from django.db import models
from shop.models import product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    active=models.BooleanField(default=True)
    def subtotal(self):
        return self.quantity*self.products.price
    def __str__(self):
        return self.products.name

class Account(models.Model):
    acctnumber=models.CharField(max_length=200)
    accttype=models.CharField(max_length=200)
    amount=models.IntegerField()
    def subtotal(self):
        return self.acctnumber
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.CharField(max_length=100)
    order_status=models.CharField(max_length=30,default="pending")
    delivery_status = models.CharField(max_length=30, default="pending")
    no_of_items=models.IntegerField()
    TotalPrice=models.IntegerField(null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    def subtotal(self):
        return self.no_of_items*self.products.price



# aarano login cheythe ayalde details databsenu edukanam, athine add cheyanam aa field to table
#user = models.ForeignKey(User, on_delete=models.CASCADE)
# djangode builtin aya default user table for signupil ulla Username aanu User

#(auto_now_add=True) oro time date update ayit varum
#integerfield nu oru limit unde , just enter cheyanullu so charfield kodukam