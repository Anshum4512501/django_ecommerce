from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView
from store.models import Product,Order,OrderItem,Customer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.generic import TemplateView,DeleteView,DetailView,CreateView
from django.urls import reverse_lazy
from .forms import  ShippingAddressForm
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
        order,created = Order.objects.get_or_create(customer=self.request.user.customer,complete=False)
        order_items = order.orderitem_set.all()
        print("order,created",order,created)
        total_price = 0
        total_quantity = 0
        products = []
        for item in order_items:
            total_quantity += item.quantity
            total_price += item.quantity*item.product.product_price
            product = Product.objects.get(id=item.product.id)
            products.append(product)
        
        context['order_item'] = order_items
        context['order_item_quatity'] = total_quantity
        context['products'] = products
        context['total_price'] = total_price
        return context


class CartDetailView(DetailView):
    model = Product
    template_name = 'store/cart_item_detail.html'

class ItemDeleteView(DeleteView):
    model = OrderItem        
    success_url= reverse_lazy('cart')
    template_name = 'store/confirm_delete.html'
    pk_url_kwarg = 'id' 
   
    def get_object(self):
        self.object = super().get_object()
        print("Self Object",self.object)
        return self.object
class CheckoutView(CreateView):
    form_class =   ShippingAddressForm
    template_name = 'store/shipping_address.html'
    def get_context_data(self, *args, **kwargs):
        context = super(CheckoutView,self).get_context_data(*args, **kwargs)
        order,created = Order.objects.get_or_create(customer=self.request.user.customer,complete=False)
        order_items = order.orderitem_set.all()
        print("order,created",order,created)
        total_price = 0
        total_quantity = 0
        products = []
        for item in order_items:
            total_quantity += item.quantity
            total_price += item.quantity*item.product.product_price
            product = Product.objects.get(id=item.product.id)
            products.append(product)
        
        context['order_item'] = order_items
        context['order_item_quatity'] = total_quantity
        context['products'] = products
        context['total_price'] = total_price
        return context   

@csrf_exempt
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

# return render(request,'store/cart.html',{'order_item':order_item})    