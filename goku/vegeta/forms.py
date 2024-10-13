
from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'summary')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Enter Title"}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'value': '','type':'hidden', 'id':'author'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', "placeholder":"Write a short overview of your topic"}),
            
        }