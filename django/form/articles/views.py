from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm
# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST) # request.POST를 이용해서 form의 내용을 미리 채워놓는다
        if form.is_valid():  # form이 정해 놓은 조건 (길이, 입력 데이터의 유무)를 충족하면
            article = form.save() # 사용자가 입력한 정보와 모델 정보를 둘다 갖고 있기 때문에 
            # title = form.cleaned_data['title']      #('title') # form의 검증을 통과한 데이터만 받아온다.
            # content = form.cleaned_data.get('content') # 딕셔너리 함수 get
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm() # 인스턴스 생성
        
    return render(request, 'form.html', {'form':form})
    
def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article':article})
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance = article) # request.POST를 이용해서 form의 내용을 미리 채워놓는다
        if form.is_valid():  # form이 정해 놓은 조건 (길이, 입력 데이터의 유무)를 충족하면
            article = form.save() # 사용자가 입력한 정보와 모델 정보를 둘다 갖고 있기 때문에 
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm(instance=article) # 인스턴스 생성
        
    return render(request, 'form.html', {'form':form})
    