from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.s
def home (request):
    return render(request, "authentication/index.html")

def login (request):
    if request.user.is_authenticated:
        return render(request, 'authentication/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'authentication/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'authentication/login.html', {'form': form})

def signup (request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'authentication/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'authentication/signup.html', {'form': form})
    
def signout(request):
    logout(request)
    return redirect('/')

def profile(request):
    return render(request, "authentication/profile.html")
