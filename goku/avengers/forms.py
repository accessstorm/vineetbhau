from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field
    first_name = forms.CharField(max_length=30, required=True)  # Add first name field
    last_name = forms.CharField(max_length=30, required=True)  # Add last name field

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']  # Specify field order
