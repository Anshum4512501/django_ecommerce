from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from store.models import Product
# Create your views here.


class ProductListingView(ListView):
    model = Product
    template_name = 'store/product_listing.html'
    context_object_name = 'products'
