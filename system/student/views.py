from django.shortcuts import render
from .form import LoginForm
# Create your views here.
from django.shortcuts import  HttpResponseRedirect, render, redirect, get_object_or_404
# Create your views here.
from django.contrib import messages
from .form import  LoginForm
from django.views.generic import UpdateView,ListView,DetailView
from django.contrib.auth.models import User
from django.contrib.auth import  login, authenticate, logout
import datetime
from django.db.models.query_utils import Q
from django.urls import reverse


def home(request):
    return render(request, "pages/home.html")



def login_page(request):
    """
    user-~ to login with their prefered choice and stuffs 
    authenticating user

    Args:
        request (_type_): _description_
    """
    form = LoginForm()
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=  username, password = password)
        if user is not None and  user.is_active:
            login(request,user)
            messages.success(request,"Login successful" )
            return redirect('home')
        else:
            messages.error(request, "details error, do you forget your password?")
            
    else:
        form = LoginForm()
        messages.success(request, "welcome back,")
        
    return render(request,"auth/login.html", {"form":form})

def logout_page(request):
    logout(request)
    return redirect('home')