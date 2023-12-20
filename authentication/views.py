from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import logging
from ministration.models import Ministration
from doctors.models import Doctors 
from django.contrib.auth.decorators import user_passes_test, login_required
from authrole.custom_context import user_is_doctor,user_is_admin

logger = logging.getLogger(__name__)

User = get_user_model()

# Create your views here
def home(request):
    ministrations = Ministration.objects.all()[:3]
    doc = Doctors.objects.all()[:3]
    return render(request, "authentication/main.html", {'ministrations': ministrations, 'doc': doc})


@user_passes_test(lambda u: user_is_doctor(u), login_url='login')
def static(request):
    return render(request, "authentication/doctor.html")


@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def index (request):
    return render (request,"admin/dashboard.html")


def login(request):
    if request.user.is_authenticated:
        if user_is_doctor(request.user):
            return redirect('/index')  
        elif user_is_admin(request.user):
            return redirect('/admin')  
        else:
            return redirect('profile') 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user_is_doctor(user):
                return redirect('/index')
            elif user_is_admin(user):
                return redirect('/admin')
            else:
                return redirect('profile')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'authentication/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})
    

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')  
        confirm_password = request.POST.get('password2')  

        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already exists. Please choose a different one.')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered. Please use a different email.')
            return render(request, 'authentication/signup.html')

        # Create the user account
        user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email)
        # Authenticate the user and log them in
        auth_login(request, user)

        return redirect('/')
    else:
        return render(request, 'authentication/signup.html')
    

def signout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def profile(request):
    return render(request, "authentication/profile.html")


@login_required(login_url='/login')
def edit_profile(request):
    user_to_edit = request.user

    if request.method == 'POST':
        user_to_edit.first_name = request.POST.get('first_name')
        user_to_edit.last_name = request.POST.get('last_name')
        user_to_edit.email = request.POST.get('email')

        user_to_edit.save()

        messages.success(request, 'Updated information successfully!')
        return redirect('profile')

    return render(request, 'authentication/edit_profile.html', {'user_to_edit': user_to_edit})

