from django.urls import path

from store.views import ProductListingView
app_name = 'store'

urlpatterns = [
    path('',ProductListingView.as_view(),name = 'all_products'),
]