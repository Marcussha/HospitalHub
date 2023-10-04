from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Client
# Create your views here.

def index (request): 
    clients = Client.objects.all()
    return render(request, "customers/index.html",{'clients': clients})

def create(request):
    clients = Client.objects.all()
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')
        sex = request.POST.get('sex')

        # Check if either the full name or email already exists in the database
        if Client.objects.filter(email=email) or  Client.objects.filter(telephone=telephone).exists(): 
            messages.error(request, 'A client with the same email or telephone already exists.')
        else:
            try:
                # Neither the full name nor email is a duplicate, create the Client object
                Client.objects.create(
                    fullname=fullname,
                    email=email,
                    telephone=telephone,
                    birthday=birthday,
                    address=address,
                    sex=sex,
                )
                return redirect('/customers/create')
            except Exception as e:
                messages.error(request, 'An error occurred while creating the client.')

    return render(request, "customers/create.html", {'clients': clients})

def clear(request, id):
    clients = Client.objects.get( id =id)
    clients.delete()
    return redirect('/customers')  


