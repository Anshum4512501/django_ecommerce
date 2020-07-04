from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView
from store.models import Product,Order,OrderItem,Customer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.generic import TemplateView
# Create your views here.


class ProductListingView(ListView):
    model = Product
    template_name = 'store/product_listing.html'
    context_object_name = 'products'
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListingView,self).get_context_data(*args, **kwargs)
        order,created = Order.objects.get_or_create(customer=self.request.user.customer,complete=False)
        order_items = order.orderitem_set.all()
        total_quantity = 0
        for item in order_items:
            total_quantity += item.quantity
        context['order_item'] = order_items
        context['order_item_quatity'] = total_quantity
        return context
        
class CartView(TemplateView):
    template_name = 'store/cart.html'
    def get_context_data(self, *args, **kwargs):
        context = super(CartView,self).get_context_data(*args, **kwargs)
        context['order_item'] = OrderItem.objects.all()
        return context
    
        

# @csrf_exempt
def update_cart(request):
    print(request.body)
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
        order_item.get_increment_quantity()
        order_item.save()
        return render(request,'store/cart.html',{'order_item':order_item})
    return JsonResponse("update comming from server...%s...%s.....%s....order_item%s....created....%s"%(json_data,product,customer,order_item,created),safe=False)