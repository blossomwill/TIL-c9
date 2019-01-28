from django.shortcuts import render
from .models import Post

# Create your views here.
# view.py -> urls.py -> .html
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    # GET은 throw.html의 method get을 의미하고 get은 dict의 get
    
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    return render(request, 'create.html')
    
def index(request):
    # All Post
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

