
from django.contrib import admin
from django.urls import path, include
from .views import home, login_page, logout_page, signup, viewprofile, standing, generate_idAndtimetable, updateimag





urlpatterns = [
      path('', login_page, name ="login"),
    path('logout', logout_page, name="logout"),
    path('signup', signup, name ="signup" ),
    path("profile/<username>", viewprofile, name="profile"),
    path("standing/",standing, name="standing"),
    path("genarating..../", generate_idAndtimetable, name="generate"),
    path("imageupdate/<slug:slug>", updateimag.as_view(), name="img-update"),
    
]

