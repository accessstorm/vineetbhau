from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm
from .models import Post
# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

class PostView(ListView):
    model = Post
    template_name = 'vineet.html'
    ordering = ['-post_date']
    #ordering = ['-id']
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pookie.html'
    
class ShowView(DetailView):
    model = Post
    template_name = 'thanos.html'
    
    