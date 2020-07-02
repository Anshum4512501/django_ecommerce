from django.shortcuts import render
from userauthentication.forms import CustomUserCreationForm,UserLoginForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class UserCreationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/userauth/login/'
    template_name = 'userauth/user_create.html'

class UserLoginView(LoginView):
    template_name= 'userauth/user_login.html'
    form_class = UserLoginForm
    # success_url = '/store/'
    

class UserLogoutView(LogoutView):
    redirect_field_name = 'login'
