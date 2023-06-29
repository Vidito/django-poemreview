from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import AccountUpdateForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': AccountUpdateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'form': AccountUpdateForm, 'error': 'Username already exists'})
        else:
            return render(request, 'signup.html', {'form': AccountUpdateForm, 'error': 'Passwords do not match'})
        

def logoutaccount(request): 
    logout(request)
    return redirect('home')


def loginaccount(request): 
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form':LoginForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password']) 
        if user is None:
            return render(request,'loginaccount.html', {'form': LoginForm, 'error': 'username and password donot match'})
        else: 
            login(request,user)
            return redirect('home')