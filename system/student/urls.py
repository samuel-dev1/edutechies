
from django.contrib import admin
from django.urls import path, include
from .views import home, login_page, logout_page, signup, viewprofile






urlpatterns = [
    path("", home , name ="home"),
      path('login', login_page, name ="login"),
    path('logout', logout_page, name="logout"),
    path('signup', signup, name ="signup" ),
    path("profile/<username>", viewprofile, name="profile"),
]

