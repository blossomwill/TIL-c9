from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image',]
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='')
    class Meta:
        model = Comment
        fields = ['content']
        