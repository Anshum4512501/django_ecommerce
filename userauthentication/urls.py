from django.urls import path

from .views import UserCreationView,UserLoginView,UserLogoutView
app_name = 'userauth'

urlpatterns = [
    path('login/',UserLoginView.as_view(),name = 'login'),
    path('logout/',UserLogoutView.as_view(),name = 'logout'),
    path('register/',UserCreationView.as_view(),name ='register')
]