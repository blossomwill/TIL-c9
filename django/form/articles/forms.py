from django import forms
from .models import Article

class ArticleForm(forms.Form):
    title = forms.CharField(label='제목')   # forms에서 가져온 CharFiled()다
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': '내용을 입력하세요.',
    }))
    
class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article # Article model을 가져오겠다.
        fields = ['title', 'content'] # 2가지에 대한 input을 만들겠다
        