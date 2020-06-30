from django.contrib import admin
from .models import Product,OrderItem,Customer,Order,ShippingAddress
# Register your models here.


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ShippingAddress)