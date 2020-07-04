from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    cusotmer = models.OneToOneField(User,on_delete=models.CASCADE)
    name  = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name                =   models.CharField(max_length= 100,default=None)
    product_price       =   models.FloatField(null=False,blank=False,default=None)
    product_description =   models.TextField(default=None)
    product_image       =   models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
                
class Order(models.Model):
    customer  = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False ,null = True,blank = True)
    transaction_id = models.CharField(max_length = 100,null =200)

    def __str__(self):
        return ("OrderId" + str(self.id)) 

            
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_increment_quantity(self):
        self.quantity+=1    
    def get_decrement_quantity(self):
        self.quantity-=1    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length = 100,null=True)
    city = models.CharField(max_length = 100,null=True)
    state = models.CharField(max_length = 100,null=True)
    zipcode = models.CharField(max_length = 100,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.city

