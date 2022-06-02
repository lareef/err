from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name')
        field_classes = {'username': UsernameField}
