from django.urls import path
from . import views
from .models import Post
from .views import PostView, AddPost, ShowView

urlpatterns = [
    path('', views.home, name='home'),
    
    
    
    
    path('vineet.html', PostView.as_view(), name="vineet"),
    
    path('thanos/<int:pk>', ShowView.as_view(), name="thanos"),
    path('pookie/', AddPost.as_view(), name="pookie"),
]