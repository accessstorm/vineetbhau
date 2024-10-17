from django.shortcuts import render
from django.views import generic
#from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

class UserRegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm  # Use the custom form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
