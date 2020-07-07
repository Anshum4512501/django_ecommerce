from store.models import Customer,OrderItem,Order,Product
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
import json

class TestMixin():
    def get_data(self,request):
        json_data = json.loads(request.body)
        product = get_object_or_404(Product,pk=json_data['product_id'])
        user = request.user
        customer,created = Customer.objects.get_or_create(cusotmer=user,name=user.username)
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        print(order)
        order_item,created  = OrderItem.objects.get_or_create(product=product,order=order)
        print("order_item,created",order_item,created)
        print("product_id ",json_data['product_id'])
        if json_data['action']=='add':
            print("inside add action")
            order_item.get_increment_quantity()
            order_item.save()
            return JsonResponse("update comming from server...%s...%s.....%s....order_item%s....created....%s"%(json_data,product,customer,order_item,created),safe=False)
        elif json_data['action']=='remove':
            print("inside remove action")
            order_item.get_decrement_quantity()
            order_item.save()
            if order_item.quantity<=0:
                order_item.delete()
            return JsonResponse("update comming from server...%s...%s.....%s....order_item%s....created....%s.....order_quantity%s.."%(json_data,product,customer,order_item,created,order_item.quantity),safe=False)
