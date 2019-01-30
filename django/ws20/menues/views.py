from django.shortcuts import render, redirect
from .models import Question, Choice
# Create your views here.

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    question = Question(title=title)
    question.save()
    return redirect('posts:detail', question.pk)
    
def index(request):
    question = Question.objects.last()
    return render(request, 'index.html',{'question':question}) 
    
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'detail.html', {'question': question})