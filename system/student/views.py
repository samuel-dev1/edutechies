from django.shortcuts import render
from .form import LoginForm, signupform
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
from django.contrib.auth.decorators import login_required


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
        
    return render(request,"auth/login.html", {"form":form})

def logout_page(request):
    logout(request)
    return redirect('home')
def signup(request):
    """
    for signing user which will be 
    over ride soon;
    contain form from form.py, and passed message to know if its error or success
    
    """
    
    #form here
    form = signupform()
    if request.method == "POST":
        #sign up form passed into request
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile created login to continue")
            return redirect('login')
        else:
            messages.error(request, "Registration failed! kindly check your details ")
    else:
        # else if niot working this should prevenet futher auth. errror
        form =signupform()
    return render(request, "auth/signup.html", {"form":form})

@login_required
def viewprofile(request, username):
    username = request.user.username
    print(username)
    return render (request, "pages/view.html")
    