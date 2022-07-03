from ctypes import LibraryLoader
from django import forms
from django.contrib.auth import get_user_model

from .models import Articulo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

User = get_user_model()

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class RegisterForm(UserCreationForm):
    
    class Meta:
      
        model = User
        fields = ["username", 
        "first_name", 
        "last_name", 
        "email", 
        "password1", 
        "password2"]
