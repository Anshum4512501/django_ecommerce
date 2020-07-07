from django.urls import path

from store.views import ProductListingView,update_cart,CartView,ItemDeleteView,CartDetailView,CheckoutView
from django.views.generic import TemplateView
app_name = 'store'

urlpatterns = [
    path('',ProductListingView.as_view(),name = 'all_products'),
    path('update-cart/',update_cart,name ='update-cart'),
    path('cart/',CartView.as_view(),name ='cart'),
    path('cart/place_order',CheckoutView.as_view(),name ='checkout'),
    path('item/delete/<int:id>',ItemDeleteView.as_view(),name ='delete'),
    path('detail/<slug:pk>',CartDetailView.as_view(),name ='detail'),
]