from django.shortcuts import render,redirect
from ministration.forms import MinistrationForm
from ministration.models import Ministration


# Create your views here.

def index (request):
    ministrations = Ministration.objects.all()
    return render (request, "ministration/index.html",{'ministrations': ministrations})

def create (request):
    if request.method == "POST":
        form = MinistrationForm (request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect ("/services")
            except:
                pass
    else:
        form = MinistrationForm()
        return render (request,'ministration/create.html', {'form':form})
    
def edit (request, id):
    ministration = Ministration.objects.get( minisid = id)
    return render (request, "ministration/edit.html",{'ministration': ministration})

def update(request, id):  
    ministration = Ministration.objects.get( minisid = id) 
    form = MinistrationForm( request.POST, instance = ministration)  
    if form.is_valid():  
        form.save()  
        return redirect("/services")  
    return render(request, "ministration/edit.html", {'ministration': ministration})  

def clear(request, id):
    ministration = Ministration.objects.get(minisid=id)
    ministration.delete()
    return redirect('/services')