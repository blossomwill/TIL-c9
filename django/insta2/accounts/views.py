from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method=="POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('posts:list')
    else:
        signup_form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})
        
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method=="POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect(request.GET.get('next') or 'posts:list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})

def logout(request):    
    auth_logout(request)
    return redirect('posts:list')
    
def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people': people})
    
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('people',request.user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        return render(request, 'accounts/update.html', {'user_change_form': user_change_form})

def delete(request):
    if request.method =="POST":
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'accounts/delete.html')
    

def follow(request, user_id):
    people = get_object_or_404(User, id=user_id)
    
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else:
        people.followers.add(request.user)
    return redirect('people', people.username)
    