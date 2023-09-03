from django.shortcuts import render, redirect
from roles.models import AuthGroup
from .forms import RoleForm

# Create your views here.

def create (request):
    if request.method == "POST":  
        form = RoleForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/roles')  
            except:  
                pass
    else:  
        form = RoleForm()
    return render(request,"role/create.html",{'form': form})


def index (request): 
    roles = AuthGroup.objects.all()
    return render(request, "role/index.html",{'roles': roles})

def edit (request, id):
    role = AuthGroup.objects.get( id =id)
    return render(request, "role/edit.html", {'role': role})

def update(request, id):
    role = AuthGroup.objects.get(id =id)
    form = RoleForm(request.POST, instance = role)
    if form.is_valid():
        form.save()
        return redirect("/roles")
    return render(request,'role/edit.html', {'roles':role})

def clear(request, id):
    role = AuthGroup.objects.get( id =id)
    role.delete()
    return redirect('/roles')  

