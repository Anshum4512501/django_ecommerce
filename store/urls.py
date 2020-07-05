from django.urls import path

from store.views import ProductListingView,update_cart,CartView,ItemDelete
from django.views.generic import TemplateView
app_name = 'store'

urlpatterns = [
    path('',ProductListingView.as_view(),name = 'all_products'),
    path('update-cart/',update_cart,name ='update-cart'),
    path('cart/',CartView.as_view(),name ='cart'),
    path('item/delete',ItemDelete.as_view(),name ='delete'),
]