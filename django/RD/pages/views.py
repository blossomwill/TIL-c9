from django.shortcuts import render, redirect
from .models import post

# Create your views here.
def index(request):
    posts = post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def hello(request, name):
    return render(request, 'hello.html', {'name':name})
    
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    posta = post(title=title, content=content)
    posta.save()
    return redirect('pages:detail', posta.pk)
    
def detail(request, post_id):
    posta = post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'posta':posta})
    
def delete(request, post_id):
    posta = post.objects.get(pk=post_id)
    posta.delete()
    return redirect('pages:list')
    
   