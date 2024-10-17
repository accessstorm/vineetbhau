
from django import forms
from .models import Post


choices = [('Semester-1', 'Semester-1'), ('Semester-2', 'Semester-2'), ('Semester-3', 'Semester-3'), ('Semester-4', 'Semester-4'), ('Semester-5', 'Semester-5'), ('Semester-6', 'Semester-6'), ('Semester-7', 'Semester-7'), ('Semester-8', 'Semester-8')]
#choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Subject', 'author', 'Marks', 'Semester')
        
        widgets = {
            'Subject': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Enter Title"}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '','type':'hidden', 'id':'author'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'Marks': forms.TextInput(attrs={'class': 'form-control'}),
            'Semester': forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            
        }