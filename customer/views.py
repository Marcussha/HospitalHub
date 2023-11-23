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

        if Client.objects.filter(email=email) or  Client.objects.filter(telephone=telephone).exists(): 
            messages.error(request, 'A client with the same email or telephone already exists.')
        else:
            try:
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

def edit(request, id):
    client = Client.objects.all()
    return render(request, 'customers/edit.html', {'client': client})

def update(request, id):
    client = Client.objects.all()

    if request.method == 'POST':
        try:
            client.fullname = request.POST.get('fullname')
            client.email = request.POST.get('email')
            client.telephone = request.POST.get('telephone')
            client.birthday = request.POST.get('birthday')
            client.address = request.POST.get('address')
            client.sex = request.POST.get('sex')
            
            client.save()

            messages.success(request, 'Client details updated successfully.')
            return redirect('/customers')
        except Exception as e:
            messages.error(request, f'An error occurred while updating the client: {e}')

    return render(request, 'customers/edit.html', {'client': client})


def clear(request, id):
    clients = Client.objects.get( id =id)
    clients.delete()
    return redirect('/customers')  


