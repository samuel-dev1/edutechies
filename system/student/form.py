from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    """
    ordinary form user to login into their account..
    """
    username = forms.CharField(label= "Username", widget=forms.TextInput(attrs={"placeholder":"username"}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'placeholder':"password"}))
    