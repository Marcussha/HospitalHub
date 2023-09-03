from django.shortcuts import render,redirect
from .models import Client

# Create your views here.

def index (request): 
    clients = Client.objects.all()
    return render(request, "customers/index.html",{'clients': clients})

def create(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        birthday = request.POST.get('birthday')
        age = request.POST.get('age')
        sex = request.POST.get('sex')


        try:
            Client.objects.create(
                fullname=fullname,
                email=email,
                telephone=telephone,
                birthday=birthday,
                age=age,
                sex=sex,

            )
            return redirect('/customers')  
        except Exception as e:
            print("Error:", str(e))

    return render(request, "customers/create.html",)

def clear(request, id):
    clients = Client.objects.get( id =id)
    clients.delete()
    return redirect('/customers')  

