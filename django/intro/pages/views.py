from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')

# Template variable
def dinner(request):
    menu = ["족발", "햄버거", "치킨", "초밥"]
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': pick})
    
# Variable routing
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def lotto(request):
    numbers = range(1,46)
    lottos = random.sample(numbers, 6)
    return render(request, 'lotto.html', {'lottos': lottos})
    
def info(request, phonenum):
    return render(request, 'info.html', {'phone': phonenum})
    
# Form tag
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'message': message})
    
# Form 외부로 요청
def naver(request):
    return render(request, 'naver.html')
    
    
# Bootstrap
def bootstrap(request):
    return render(request, 'bootstrap.html')
    