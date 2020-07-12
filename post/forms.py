from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message']
        widgets = {'message': forms.TextInput(attrs={'class' : 'mdl-textfield__input'}) }
    
    
