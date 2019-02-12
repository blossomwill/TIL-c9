from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login # login이라는 이름을 auto_login으로 변경
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('post:list')
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid(): # 중복된 아이디가 없다면, 비밀번호가 짧지 않다면 등등
            user = form.save()
            auth_login(request, form.get_user()) # 회원가입을 하는 동시에 유저를 생성하고 로그인까지한다
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Session을 create한다
def login(request): 
    if request.user.is_authenticated: # user가 로그인 되어있으면 로그인 페이지를 못보게 한다.
        return redirect('post:list')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # 내부적으로 session을 create한다.
            return redirect(request.GET.get('next') or 'posts:list') # 왜 바로 new로 넘어가지??
            #=> 주소의 next 다음에 있는 값이 들어오게 된다
            # next란 값이 없으면 리스트페이지(posts:list)를 나타낸다.
    else:
        form = AuthenticationForm()
     
    return render(request, 'login.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
    